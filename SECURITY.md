---

## 📄 `SECURITY.md`

```markdown
# Security Policy

We take security seriously. Please follow this policy to report vulnerabilities.

## Supported Versions

We aim to support the latest `main` branch commits and the most recent tagged releases (e.g., `vX.Y.Z`). Older releases may receive fixes at maintainers’ discretion.

## Reporting a Vulnerability

- **Do not open public issues** for security vulnerabilities.
- Email the maintainers: **rodrigonpaiva@gmail.com**
- Include:
  - Affected versions/commit hashes
  - Reproduction steps or PoC
  - Impact assessment (confidentiality/integrity/availability)
  - Any potential mitigations/workarounds

We will acknowledge receipt within 72 hours and provide a remediation timeline when possible.

## Coordinated Disclosure

- We prefer a responsible disclosure window of **90 days**.
- We will work with you to coordinate public disclosure after a fix is available and users have had reasonable time to update.

## Scope

- Application code in this repository (`src/`, `infra/`)
- Build/CI pipeline definitions (`.github/workflows/`)
- Container images produced by this repo

**Out of scope** examples:
- Social engineering attacks
- Denial-of-service via unrealistic resource limits
- Vulnerabilities requiring privileged local access on the user’s host

## Handling Secrets

- Never commit secrets or credentials.
- Use environment variables, vaults, or GitHub Actions secrets.
- Our tooling includes **Gitleaks** to prevent accidental leaks.

## Dependency Security

- We periodically update Python dependencies.
- Security scans run in CI via pre-commit hooks (Bandit) and dependabot (optional).
- If a critical issue is found in a dependency, please include a link to the advisory (CVE/GHSA).

## Contact

- Primary: **rodrigonpaiva@gmail.com**
- Backup: open a **Private Security Advisory** in GitHub (if available in your org).

Thank you for helping keep the project and its users safe.
