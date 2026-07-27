---
layout: default
title: VPN Performance Benchmark Methodology
description: A reproducible methodology for latency, throughput, packet loss, connection success, and reconnect testing.
---

# VPN Performance Benchmark Methodology

This methodology defines how public VPN performance results should be collected and interpreted. It does not contain a fabricated benchmark or guarantee future performance.

## Required metadata

Each test record includes:

- UTC timestamp and unique test identifier;
- client version, operating system, and device class;
- protocol label and methodology version;
- test country or region and network type;
- sample count;
- whether the result is an internal test or a named third-party assessment.

Private node addresses, credentials, and user information are excluded.

## Metrics

- Median connection latency in milliseconds
- 95th-percentile jitter in milliseconds
- Packet loss percentage
- Median download and upload throughput in Mbps
- Connection success percentage
- Median reconnect time in milliseconds

## Test sequence

1. Record the baseline network without a VPN.
2. Fix the device, network, destination, and sampling window.
3. Warm up the network without counting warm-up samples.
4. Run repeated connection and transfer samples.
5. Record failures; do not silently discard them.
6. Publish aggregate output and the machine-readable dataset.
7. State known limitations, outages, and excluded samples.

## Interpretation

Results from one country, provider, device, or hour must not be generalized to every user. Median and percentile measurements are preferred over a single “best” sample.

Comparisons require equivalent test conditions. A change in provider, route, device, test server, or sampling window must be disclosed.

## Dataset validation

Public CSV files follow [benchmark.schema.json](../../data/schemas/benchmark.schema.json) and can be checked with:

```bash
python3 tools/validate_benchmark.py data/performance/template.csv
```
