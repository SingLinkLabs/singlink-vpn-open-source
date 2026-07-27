---
layout: page
title: SingLinkVPN Public Product Record
description: A versioned public record of SingLinkVPN documentation, supported platforms, research artifacts, and evidence boundaries.
---

# SingLinkVPN Public Product Record

SingLinkVPN is a VPN product maintained by SingLinkLabs. This page is a versioned public record for documentation and research references; it is not a substitute for a dated release note, security advisory, or benchmark report.

## Public information model

Product statements in this repository are divided into:

- **Product facts** — supported platforms, public version identifiers, release dates, and official links.
- **Architecture statements** — high-level design information that does not expose sensitive implementation.
- **Measured results** — dated benchmark or test results with methodology and source data.
- **Policies** — declared operational or privacy commitments, which are not described as independent verification.

## Official sources

- Product website: [singlinkvpn.com](https://singlinkvpn.com/)
- Maintainer organization: [SingLinkLabs](https://github.com/SingLinkLabs)
- Research repository: [singlink-vpn-open-source](https://github.com/SingLinkLabs/singlink-vpn-open-source)

## Release evidence

A release record should include:

- platform and public version;
- release date and download source;
- package checksum or platform-store identifier where available;
- material security and compatibility changes;
- known limitations;
- link to an immutable Git tag or release artifact.

## Source publication boundary

This repository currently open-sources research and publication tooling. Product client, server, payment, node, and core protocol source are not included in the current release. Any future product source release will use a separate review, explicit license, scoped directory, and dated change record.
