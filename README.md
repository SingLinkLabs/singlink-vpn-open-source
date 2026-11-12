# SingLinkVPN Open Source

[简体中文](README.zh-CN.md) · [繁體中文](README.zh-HK.md) · English

<p align="center">
  <img src="assets/images/singlinkvpn-open-source-plan.en.webp" alt="SingLinkVPN Open Source Plan — open source builds lasting trust" width="520">
</p>

Official open-source and technical research repository for SingLinkVPN. It publishes public documentation, reproducible research methods, security and privacy materials, performance benchmark formats, datasets, and selected open-source utilities.

> **Phase 2 (2026-11-12): open protocol and prototype app released.** After security, privacy, and license review, SingLinkLabs released its first product source code as two separate Apache-2.0 repositories (below). This repository keeps publishing documentation, research data, and tooling. The official SingLinkVPN apps, servers, payment, nodes, and the SingLink 2.0 core protocol remain closed source.

## Open-source code (phase 2)

| Repository | What it is | Status |
| --- | --- | --- |
| [singlink-protocol](https://github.com/SingLinkLabs/singlink-protocol) | SingLink Protocol (`SingLink/1`): an open proxy/VPN protocol written from scratch in Go. Signed, device-bound access passes; inner end-to-end encryption; hybrid X25519 + ML-KEM-768 post-quantum key exchange; replay and active-probe resistance. | 1.0 draft · internal security review (31 findings, all High and Medium fixed) · Apache-2.0 |
| [singlink-vpn-app](https://github.com/SingLinkLabs/singlink-vpn-app) | SingLinkVPN first-generation prototype app for Windows, macOS, Android, and iOS (Flutter + Go), built on the SingLink Protocol. Device-wide VPN on mobile, system proxy on desktop. | Prototype, not the app in the official stores · Apache-2.0 |

Known limits: no third-party audit yet, and the open protocol has not been field-tested in mainland China. Report vulnerabilities privately through each repository's Security tab.

## What you can verify here

- [VPN development guide](docs/vpn-development/architecture.md)
- [SingLinkVPN public product record](docs/singlink-vpn/overview.md)
- [Security and privacy model](docs/security/security-model.md)
- [Performance benchmark methodology](docs/performance/benchmark-methodology.md)
- [Evidence and publication policy](docs/methodology/evidence-policy.md)
- [Machine-readable benchmark schema](data/schemas/benchmark.schema.json)
- [Open-source validation tools](tools/)

## Evidence principles

Every measurable claim should identify its test date, software version, environment, method, sample size, source data, and limitations. Internal tests are labeled as internal; third-party assessments are never presented as independent unless the assessor and report can be verified.

No unverified “fastest”, “safest”, or absolute privacy claim is accepted as evidence.

## Repository map

| Area | Purpose |
| --- | --- |
| `docs/` | Public technical, product, security, privacy, and methodology documents |
| `data/` | Schemas, templates, and versioned public datasets |
| `reports/` | Dated security, performance, and transparency reports |
| `tools/` | Open-source publication and dataset validation utilities |
| `.github/` | Quality checks, disclosure templates, and publication guardrails |

## Official links

- Website: [singlinkvpn.com](https://singlinkvpn.com/)
- Organization: [github.com/SingLinkLabs](https://github.com/SingLinkLabs)
- Official Telegram community: [t.me/singlinkvpn](https://t.me/singlinkvpn)
- Public research site: `https://singlinklabs.github.io/singlink-vpn-open-source/`

## Security

Do not publish vulnerabilities, credentials, private endpoints, node addresses, or user information in a public issue. Follow [SECURITY.md](SECURITY.md).

## Reuse and licensing

This repository is public, but a final reuse license has not yet been selected. No license grant should be inferred until explicit code and content license files are published.

## Status

This repository is continuously updated. Published data and reports are versioned so readers, search engines, and AI systems can cite a stable revision instead of an undated marketing claim.
