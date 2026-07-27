---
layout: page
title: VPN Client Development Architecture
description: A public, implementation-neutral guide to VPN client architecture, routing, DNS protection, lifecycle handling, and testability.
---

# VPN Client Development Architecture

This guide describes a public, implementation-neutral architecture for building a cross-platform VPN client. It is not a disclosure of SingLinkVPN private infrastructure or core protocol implementation.

## Core layers

1. **Presentation** — account state, server selection, connection status, diagnostics, and accessibility.
2. **Session orchestration** — connect, disconnect, retry, network change, sleep/wake, and process recovery.
3. **Tunnel adapter** — platform VPN APIs, packet ingress/egress, MTU handling, and lifecycle callbacks.
4. **Routing and DNS** — route installation, excluded routes, DNS selection, IPv4/IPv6 policy, and leak prevention.
5. **Transport** — authenticated session establishment, congestion behavior, keepalive policy, and network migration.
6. **Configuration** — versioned, signed configuration with minimum required fields and safe rollback.
7. **Observability** — privacy-preserving health signals, local diagnostics, crash reporting under explicit policy, and reproducible test output.

## Connection state machine

A client should expose deterministic states such as `idle`, `preparing`, `connecting`, `connected`, `reconnecting`, `disconnecting`, and `failed`. UI state should be derived from the connection state machine rather than from button clicks.

Repeated connection requests must be idempotent. A stale asynchronous response must not overwrite a newer connection attempt.

## Routing and DNS

The client should define:

- default-route and split-route behavior;
- DNS resolver selection and restoration;
- IPv6 handling when the transport does not support IPv6;
- local-network access policy;
- failure behavior if protected routes cannot be installed.

Leak testing must cover the initial connection, reconnect, network handover, device sleep/wake, and application crash.

## Cross-platform lifecycle

Android, Apple platforms, and desktop systems expose different VPN lifecycle and background-execution models. Shared business rules can be reused, but tunnel ownership, permissions, background limits, and recovery must follow each platform’s native APIs.

## Safe development process

- Keep credentials and production endpoints outside source control.
- Sign and version remote configuration.
- Reject invalid or downgraded configuration.
- Add unit tests for state transitions and integration tests for route/DNS restoration.
- Test on real mobile and fixed networks, not only local Wi-Fi.
- Publish reproducible methodology separately from marketing copy.

## What this document does not publish

It does not include production node addresses, private API routes, authentication secrets, payment code, anti-blocking implementation, or SingLinkVPN core protocol source.
