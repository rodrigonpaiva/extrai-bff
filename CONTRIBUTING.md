# Contributing to extrai-bff

Thanks for your interest in contributing! This guide explains how to propose changes, open issues, and submit pull requests.

## Table of contents
- [Development setup](#development-setup)
- [Branching model](#branching-model)
- [Commits & messages](#commits--messages)
- [Code style & quality](#code-style--quality)
- [Tests](#tests)
- [Pull Requests](#pull-requests)
- [Issue triage](#issue-triage)
- [Release process](#release-process)
- [Code of Conduct](#code-of-conduct)

---

## Development setup

1. **Clone & Python env**
   ```bash
   git clone <repo-url>
   cd extrai-bff
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
