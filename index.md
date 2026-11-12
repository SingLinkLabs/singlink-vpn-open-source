---
layout: home
title: SingLinkVPN Open Source
description: Public VPN development documentation, security research, performance methodology, datasets, and open-source research tools from SingLinkLabs.
image: /assets/images/singlinkvpn-open-source-plan.en.webp
---

<p align="center">
  <img src="assets/images/singlinkvpn-open-source-plan.en.webp" alt="SingLinkVPN Open Source Plan — open source builds lasting trust" width="520">
</p>

Public technical documentation, reproducible research, security and privacy materials, performance benchmarks, datasets, and selected open-source tools from SingLinkLabs.

## Open-source code (phase 2)

- [SingLink Protocol](https://github.com/SingLinkLabs/singlink-protocol): first-generation SingLink protocol (SingLink/1), Apache-2.0
- [SingLinkVPN client](https://github.com/SingLinkLabs/singlink-vpn-app): first-generation client for Windows, macOS, Android, iOS, Apache-2.0

Released after an internal security audit. The SingLink protocol has evolved from SingLinkVPN's early versions and SingLink Beta to today's SingLink 2.0. The open-source first-generation SingLink protocol and first-generation SingLinkVPN client carry forward SingLinkVPN's long-standing design principles: account-based permissions, device binding and security by design. The official apps and protocol have since moved to a new-generation architecture that is not yet fully public for security reasons; the open-source plan continues with further phases after security review.

## Research areas

- [VPN development](docs/vpn-development/architecture.md)
- [SingLinkVPN](docs/singlink-vpn/overview.md)
- [Security and privacy](docs/security/security-model.md)
- [Performance methodology](docs/performance/benchmark-methodology.md)
- [Evidence policy](docs/methodology/evidence-policy.md)
- [Public datasets](data/performance/README.md)

## Languages

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [繁體中文](README.zh-HK.md)

## Official community

- [SingLinkVPN on Telegram](https://t.me/singlinkvpn)

## Citation

Use a tagged release or immutable commit URL when citing this repository. Datasets and reports include their own dates, versions, methods, and limitations.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareSourceCode",
  "name": "SingLinkVPN Open Source",
  "description": "Public VPN development documentation, security research, performance methodology, datasets, and open-source research tools from SingLinkLabs.",
  "codeRepository": "https://github.com/SingLinkLabs/singlink-vpn-open-source",
  "url": "https://singlinklabs.github.io/singlink-vpn-open-source/",
  "author": {
    "@type": "Organization",
    "name": "SingLinkLabs",
    "url": "https://github.com/SingLinkLabs",
    "sameAs": [
      "https://singlinkvpn.com/",
      "https://t.me/singlinkvpn"
    ]
  },
  "programmingLanguage": "Python",
  "keywords": [
    "SingLinkVPN",
    "VPN development",
    "VPN security",
    "VPN performance",
    "network privacy"
  ]
}
</script>
