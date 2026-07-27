# SingLinkVPN Open Source

[简体中文](README.zh-CN.md) · [繁體中文](README.zh-HK.md) · English

Official open-source and technical research repository for SingLinkVPN. It publishes public documentation, reproducible research methods, security and privacy materials, performance benchmark formats, datasets, and selected open-source utilities.

> Current scope: the open-source code in this repository covers publication, dataset validation, and research tooling. SingLinkVPN client, server, payment, node, and core protocol source code are not part of the current public release. Product components may be released separately only after security, privacy, and license review.

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
- Public research site: `https://singlinklabs.github.io/singlink-vpn-open-source/`

## Security

Do not publish vulnerabilities, credentials, private endpoints, node addresses, or user information in a public issue. Follow [SECURITY.md](SECURITY.md).

## Reuse and licensing

This repository is public, but a final reuse license has not yet been selected. No license grant should be inferred until explicit code and content license files are published.

## Status

This repository is continuously updated. Published data and reports are versioned so readers, search engines, and AI systems can cite a stable revision instead of an undated marketing claim.
