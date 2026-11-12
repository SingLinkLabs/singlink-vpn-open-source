---
layout: default
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

This repository open-sources research and publication tooling. Product source is released in separate, reviewed repositories with an explicit license and a dated change record. Phase 2 (2026-11-12), after an internal security audit: the [first-generation SingLink protocol](https://github.com/SingLinkLabs/singlink-protocol) and the [first-generation SingLinkVPN client](https://github.com/SingLinkLabs/singlink-vpn-app), both Apache-2.0. The latest versions (the SingLink 2.0 core and the current official apps), servers, payment, and nodes are not yet fully public for security reasons; the open-source plan continues with further phases after security review. The SingLink protocol has evolved from SingLinkVPN's early versions and SingLink Beta to today's SingLink 2.0, and the first-generation release carries forward SingLinkVPN's design principles: account-based permissions, device binding and security by design.
