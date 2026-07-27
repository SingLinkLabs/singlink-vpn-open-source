#!/usr/bin/env python3
"""Validate multilingual page mappings and rendered SEO metadata."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAPPING_PATH = ROOT / "_data" / "language_variants.json"
SITE_ORIGIN = "https://singlinklabs.github.io"
SITE_BASE_PATH = "/singlink-vpn-open-source"
LANGUAGES = ("en", "zh-Hans", "zh-Hant")
ALL_ALTERNATES = (*LANGUAGES, "x-default")
SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML_NAMESPACE = "http://www.w3.org/1999/xhtml"


class PageSEOParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.html_lang: str | None = None
        self.description: str | None = None
        self.canonical: str | None = None
        self.alternates: dict[str, str] = {}
        self.noindex = False
        self.h1_count = 0

    def handle_starttag(
        self, tag: str, attributes: list[tuple[str, str | None]]
    ) -> None:
        attrs = {key.lower(): value for key, value in attributes}
        if tag == "html":
            self.html_lang = attrs.get("lang")
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "meta":
            name = (attrs.get("name") or "").lower()
            content = attrs.get("content") or ""
            if name == "description":
                self.description = content
            elif name == "robots" and "noindex" in content.lower():
                self.noindex = True
        elif tag == "link":
            relationships = (attrs.get("rel") or "").lower().split()
            href = attrs.get("href")
            if "canonical" in relationships and href:
                self.canonical = href
            if "alternate" in relationships and attrs.get("hreflang") and href:
                self.alternates[attrs["hreflang"]] = href


def fail(message: str) -> None:
    raise ValueError(message)


def load_mapping() -> dict[str, dict[str, str]]:
    data = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not data:
        fail("Language variant mapping must be a non-empty object")
    return data


def absolute_url(page_url: str) -> str:
    if page_url == "/":
        return f"{SITE_ORIGIN}{SITE_BASE_PATH}/"
    return f"{SITE_ORIGIN}{SITE_BASE_PATH}{page_url}"


def source_path(page_url: str) -> Path:
    if page_url == "/":
        return ROOT / "index.md"
    if not page_url.endswith(".html"):
        fail(f"Mapped page URL must end in .html: {page_url}")
    return ROOT / f"{page_url.lstrip('/')[:-5]}.md"


def validate_source(mapping: dict[str, dict[str, str]]) -> None:
    canonical_urls: set[str] = set()
    for group_name, variants in mapping.items():
        if set(variants) != set(ALL_ALTERNATES):
            fail(
                f"{group_name}: expected alternates {ALL_ALTERNATES}, "
                f"got {tuple(variants)}"
            )
        if variants["x-default"] != variants["en"]:
            fail(f"{group_name}: x-default must point to the English page")

        for language in LANGUAGES:
            page_url = variants[language]
            if page_url in canonical_urls:
                fail(f"Duplicate canonical page URL: {page_url}")
            canonical_urls.add(page_url)
            if not source_path(page_url).is_file():
                fail(f"{group_name}: source file missing for {page_url}")

    head_template = (ROOT / "_includes" / "head.html").read_text(encoding="utf-8")
    for token in ("site.data.language_variants", 'rel="alternate"', "hreflang="):
        if token not in head_template:
            fail(f"Head template is missing multilingual token: {token}")

    sitemap_template = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for token in (
        "site.data.language_variants",
        'xmlns:xhtml="http://www.w3.org/1999/xhtml"',
        "xhtml:link",
        "hreflang=",
    ):
        if token not in sitemap_template:
            fail(f"Sitemap template is missing multilingual token: {token}")


def rendered_file(site_dir: Path, page_url: str) -> Path:
    if page_url == "/":
        return site_dir / "index.html"
    return site_dir / page_url.lstrip("/")


def validate_rendered_pages(
    mapping: dict[str, dict[str, str]], site_dir: Path
) -> None:
    for group_name, variants in mapping.items():
        expected_alternates = {
            language: absolute_url(page_url)
            for language, page_url in variants.items()
        }
        for language in LANGUAGES:
            page_url = variants[language]
            output_path = rendered_file(site_dir, page_url)
            if not output_path.is_file():
                fail(f"{group_name}: rendered page missing: {output_path}")

            parser = PageSEOParser()
            parser.feed(output_path.read_text(encoding="utf-8"))
            if parser.html_lang != language:
                fail(
                    f"{page_url}: html lang is {parser.html_lang!r}, "
                    f"expected {language!r}"
                )
            if parser.canonical != absolute_url(page_url):
                fail(
                    f"{page_url}: canonical is {parser.canonical!r}, "
                    f"expected {absolute_url(page_url)!r}"
                )
            if parser.alternates != expected_alternates:
                fail(
                    f"{page_url}: hreflang mapping differs from "
                    f"{expected_alternates}"
                )
            if parser.noindex:
                fail(f"{page_url}: rendered page contains noindex")
            if parser.h1_count != 1:
                fail(
                    f"{page_url}: expected exactly one h1, "
                    f"found {parser.h1_count}"
                )
            if not parser.description:
                fail(f"{page_url}: meta description is missing")
            if language.startswith("zh") and not re.search(
                r"[\u3400-\u9fff]", parser.description
            ):
                fail(f"{page_url}: Chinese meta description is not localized")


def validate_rendered_sitemap(
    mapping: dict[str, dict[str, str]], site_dir: Path
) -> None:
    sitemap_path = site_dir / "sitemap.xml"
    if not sitemap_path.is_file():
        fail("Rendered sitemap.xml is missing")

    root = ET.parse(sitemap_path).getroot()
    sitemap_entries: dict[str, dict[str, str]] = {}
    for url_node in root.findall(f"{{{SITEMAP_NAMESPACE}}}url"):
        loc = url_node.findtext(f"{{{SITEMAP_NAMESPACE}}}loc")
        if not loc:
            fail("Sitemap entry is missing loc")
        alternates = {
            node.attrib["hreflang"]: node.attrib["href"]
            for node in url_node.findall(f"{{{XHTML_NAMESPACE}}}link")
        }
        sitemap_entries[loc] = alternates

    expected_urls = {
        absolute_url(variants[language])
        for variants in mapping.values()
        for language in LANGUAGES
    }
    if set(sitemap_entries) != expected_urls:
        missing = sorted(expected_urls - set(sitemap_entries))
        unexpected = sorted(set(sitemap_entries) - expected_urls)
        fail(f"Sitemap URL mismatch; missing={missing}, unexpected={unexpected}")

    for group_name, variants in mapping.items():
        expected_alternates = {
            language: absolute_url(page_url)
            for language, page_url in variants.items()
        }
        for language in LANGUAGES:
            loc = absolute_url(variants[language])
            if sitemap_entries[loc] != expected_alternates:
                fail(f"{group_name}: sitemap alternates differ for {loc}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--site",
        type=Path,
        help="Validate rendered Jekyll output in this directory",
    )
    args = parser.parse_args()

    try:
        mapping = load_mapping()
        validate_source(mapping)
        if args.site:
            site_dir = args.site.resolve()
            validate_rendered_pages(mapping, site_dir)
            validate_rendered_sitemap(mapping, site_dir)
    except (OSError, ValueError, json.JSONDecodeError, ET.ParseError) as error:
        print(f"Multilingual SEO validation failed: {error}", file=sys.stderr)
        return 1

    page_count = len(mapping) * len(LANGUAGES)
    if args.site:
        print(f"Multilingual SEO validation passed for {page_count} rendered pages.")
    else:
        print(f"Multilingual SEO source validation passed for {page_count} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
