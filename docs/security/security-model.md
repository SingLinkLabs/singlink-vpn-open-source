---
layout: page
title: Security and Privacy Model
description: Public security evidence boundaries, threat model categories, testing requirements, and disclosure process.
---

# Security and Privacy Model

Security is documented as testable controls and explicit limitations, not as an absolute label.

## Threat categories

Public assessments should consider:

- traffic observation on the local network;
- DNS, IPv6, and WebRTC leakage;
- route loss during reconnect or network handover;
- malicious or downgraded remote configuration;
- credential exposure on the device;
- dependency and build-chain compromise;
- account abuse and unauthorized session use;
- excessive diagnostic or support-data collection.

## Evidence required

Each result must identify the affected client version, operating system, test date, network conditions, test method, expected behavior, observed behavior, and limitations.

A security policy or architecture statement is not the same as an independent audit. Third-party status requires a named assessor and a verifiable report.

## Privacy boundaries

Public datasets must not contain user identifiers, account records, billing data, support messages, production credentials, or raw production traffic. Aggregation and de-identification must be reviewed before publication.

## Responsible disclosure

Unpatched vulnerabilities are reported privately under [SECURITY.md](../../SECURITY.md). A public advisory follows remediation and identifies affected and fixed versions.
