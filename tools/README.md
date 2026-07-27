# Open-source research tools

The tools in this directory are public utilities for research-data validation and safe publication. They do not contain SingLinkVPN product source or production configuration.

## Publication guard

```bash
python3 tools/publication_guard.py
```

Checks for blocked credentials, private paths, archives, binaries, product-source file types, binary content, oversized files, and common live-secret formats.

## Benchmark validator

```bash
python3 tools/validate_benchmark.py data/performance/template.csv
```

Validates the exact CSV header and field ranges defined by the public benchmark methodology.

## Relative-link checker

```bash
python3 tools/check_relative_links.py
```

Verifies that repository-local links in Markdown files resolve to public files.
