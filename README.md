# 🧠 Bit-Block Sidekick  
### Your Intelligent DevOps, SRE, and Cloud Automation Companion

**Bit-Block Sidekick** is a lightweight, domain-aware AI agent designed to turn your **Bit-Block Starter Packs** into **self-running, self-auditing, and self-healing systems**.

Instead of starting from static templates, teams can bootstrap their infrastructure with an intelligent Sidekick that **analyzes**, **suggests**, and **automates** best practices across Terraform, Kubernetes, CI/CD, and observability stacks.

---

## 🚀 Features

- **🔍 Secure Smart Audit**  
  Scans your repo for missing guardrails (NetworkPolicies, IAM boundaries, PDBs, branch protections) and opens pull requests with fixes.

- **🏗️ Domain Packs**  
  Pre-tuned best practices for **SaaS APIs**, **AI/ML workloads**, **FinTech**, and **Data/ETL pipelines**.

- **🧩 Rego-Based Guardrails**  
  Runs OPA/Conftest policy checks before any change is applied to ensure every modification passes security and compliance gates.

- **💬 Chat-Driven Assistance**  
  Ask the Sidekick questions directly from your CLI — it explains “why” and “how” using your repo context.

- **📈 Observability Hooks**  
  Monitors Prometheus metrics or GitHub Actions logs for anomalies and posts remediation suggestions or auto-generated runbooks.

---

## ⚙️ Quickstart

### 1️⃣ Initialize for your domain
```bash
bb-sidekick init --domain saas_api
````

### 2️⃣ Run an audit and open a PR with improvements

```bash
bb-sidekick audit --open-pr
```

### 3️⃣ Ask contextual questions

```bash
bb-sidekick ask "How do I add a staging namespace securely?"
```

---

## 🧩 GitHub Action Integration

Add the following workflow to automate weekly audits and PR reviews:

```yaml
# .github/workflows/sidekick.yml
name: Bit-Block Sidekick

on:
  workflow_dispatch:
  schedule:
    - cron: "0 3 * * 1"   # Every Monday 3 AM UTC
  pull_request:

jobs:
  run:
    permissions:
      contents: write
      pull-requests: write
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install CLIs
        run: |
          sudo apt-get update && sudo apt-get install -y conftest
          curl -fsSL https://get.terraform.io | sh || true
          curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl && chmod +x kubectl && sudo mv kubectl /usr/local/bin/
      - name: Run Sidekick Audit
        run: python bitblocks-sidekick/agents/planner.py --audit --pr
      - name: Policy Check
        run: conftest test -p bitblocks-sidekick/policies/rego .
```

---

## 🔐 Built-In Safety

* ✅ **Read-Only by Default** — Sidekick never applies directly to production.
* ✅ **Policy-Gated PRs** — All changes are validated via Rego/OPA guardrails.
* ✅ **Human-Approved Merges** — PRs require authorized reviewers.
* ✅ **No Direct Writes** — Everything flows through GitOps or pull requests.

---

## 🧱 Supported Domain Packs

| Domain           | Description                           | Key Capabilities                                                |
| ---------------- | ------------------------------------- | --------------------------------------------------------------- |
| **SaaS API**     | Web/API backends and microservices    | Auto-adds NetworkPolicies, HPAs, health checks, and rate limits |
| **AI/ML App**    | GPU-based inference or model training | Resource guards, cost control, cache optimization               |
| **FinTech-Lite** | Payment and compliance apps           | TLS enforcement, secrets rotation, PCI-lean policies            |
| **Data/ETL**     | Pipelines and batch jobs              | DLQ setup, retry policies, lifecycle management                 |

---

## 💡 Philosophy

> *Move fast, but never break your cloud.*

Bit-Block Sidekick empowers startups and engineers to launch faster, safer, and smarter — with production-grade security and reliability from day one.

---

## 🧰 Stack Highlights

* **Language:** Python 3.11+
* **Policies:** OPA / Conftest (Rego)
* **Infra Support:** Terraform, Kubernetes
* **Observability:** Prometheus / Grafana
* **CI/CD:** GitHub Actions / GitLab
* **Security:** IAM Boundary / Policy Linter / NetworkPolicy Generator

---

## 🌍 Learn More

**Website:** [https://bluebit.live](https://bluebit.live)
**Docs:** Coming soon → `docs/bitblock-sidekick.md`
**Made by:** [Bluebit Information Technology Services](https://bluebit.live)

---

### 📜 License

This project is part of the **Bit-Block Starter Suite** by **Bluebit IT Services**.
All rights reserved © 2025 Bluebit Information Technology Services.

---



