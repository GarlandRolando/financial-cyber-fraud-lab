from pathlib import Path

import pandas as pd

from financial_cyber_fraud.features import build_features
from financial_cyber_fraud.metrics import alert_summary, evaluate_synthetic_labels
from financial_cyber_fraud.scoring import score_transactions


ROOT = Path(__file__).resolve().parents[1]
transactions = pd.read_csv(ROOT / "data" / "synthetic_transactions.csv")
features = build_features(transactions)
scored = score_transactions(features)

output = ROOT / "reports" / "alerts.csv"
output.parent.mkdir(parents=True, exist_ok=True)
scored.to_csv(output, index=False)

print(alert_summary(scored))
print(evaluate_synthetic_labels(scored))
print(f"Saved: {output}")
