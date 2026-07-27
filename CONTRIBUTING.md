# Contributing

Contributions that improve documentation, reproducibility, data quality, accessibility, or public research tooling are welcome.

Before opening a pull request:

1. Do not include SingLinkVPN product source code or private infrastructure information.
2. Do not include secrets, credentials, user information, private endpoints, or production logs.
3. Run `python3 tools/publication_guard.py`.
4. Run `python3 -m unittest discover -s tests -v`.
5. Explain the evidence source, method, date, and limitations for any measurable claim.

Security vulnerabilities must follow [SECURITY.md](SECURITY.md), not a public issue.
