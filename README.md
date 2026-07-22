# Financial Cyber-Fraud Lab

[![CI](https://github.com/GarlandRolando/financial-cyber-fraud-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/GarlandRolando/financial-cyber-fraud-lab/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-informational)
![Domain](https://img.shields.io/badge/Domain-Financial%20Crime%20Analytics-informational)
![Status](https://img.shields.io/badge/Status-Portfolio%20Starter-informational)

An explainable transaction-monitoring and cyber-enabled fraud analytics project
for financial crime, fraud risk, technology risk, and RegTech roles.

## Business problem

Digital payments create speed and convenience, but also enable scams, account
takeover, mule networks, unusual cross-border flows, and rapid transaction
velocity. Financial institutions need systems that prioritise alerts without
turning every customer payment into a compliance opera.

This project demonstrates how to:

1. engineer behavioural transaction features;
2. combine explainable rules with anomaly signals;
3. identify shared-device and beneficiary concentration risk;
4. prioritise investigation cases;
5. analyse alerts with SQL;
6. document assumptions and limitations; and
7. test the implementation automatically.

## Features

- Customer-relative amount anomaly
- New-beneficiary detection
- Cross-border risk indicator
- Odd-hour activity
- Transaction-velocity risk
- Shared-device risk
- Beneficiary concentration risk
- Explainable 0–100 alert score
- Priority bands: Low, Review, High, Critical
- Streamlit investigation dashboard
- SQL monitoring queries
- Synthetic labelled data for safe demonstration
- Automated tests and GitHub Actions

## Quick start

```bash
git clone https://github.com/GarlandRolando/financial-cyber-fraud-lab.git
cd financial-cyber-fraud-lab

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
pip install -e .
streamlit run app.py
```

Run tests:

```bash
pytest
```

Generate an alert file:

```bash
python scripts/generate_alerts.py
```

## Alert methodology

The starter score combines transparent indicators:

| Signal | Maximum points |
|---|---:|
| Customer-relative amount anomaly | 25 |
| High transaction velocity | 20 |
| New beneficiary | 15 |
| Cross-border payment | 10 |
| Odd-hour activity | 10 |
| Shared device | 10 |
| Concentrated beneficiary activity | 10 |

This is intentionally interpretable. Real financial institutions should
calibrate thresholds, validate models, monitor drift, document governance, and
include human investigation.

## Repository structure

```text
financial-cyber-fraud-lab/
├── app.py
├── data/
├── docs/
├── reports/
├── scripts/
├── sql/
├── src/financial_cyber_fraud/
├── tests/
├── .github/workflows/
├── pyproject.toml
└── requirements.txt
```

## Recruiter signal

This project demonstrates:

- Python and pandas;
- SQL analytics;
- fraud and AML reasoning;
- explainable risk scoring;
- feature engineering;
- data-quality checks;
- operational dashboard design;
- model governance awareness;
- automated testing; and
- financial-sector documentation.

## Roadmap

- Graph-based mule-network detection
- Supervised fraud model with precision-recall evaluation
- Investigator feedback loop
- Model drift monitoring
- Adverse-media and sanctions data adapters
- AI-agent governance controls
- DORA-style third-party dependency mapping
- Market-specific regulatory control mapping

## Important limitations

The dataset is synthetic. The rules are educational, not validated. The project
does not accuse any real person or organisation of wrongdoing and must not be
used for real investigations without governance, legal review, model validation,
and institution-specific data.

## AI assistance

This starter was created with AI assistance. The repository owner should
understand every feature, change at least one material component, and be able to
explain why false positives and false negatives matter.
