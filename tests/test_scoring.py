import pandas as pd

from financial_cyber_fraud.features import build_features
from financial_cyber_fraud.scoring import score_transactions


def test_high_risk_transaction_scores_above_normal():
    data = pd.DataFrame({
        "transaction_id": ["T1", "T2", "T3", "T4", "T5"],
        "customer_id": ["C1", "C1", "C1", "C1", "C2"],
        "beneficiary_id": ["B1", "B2", "B3", "B4", "B5"],
        "device_id": ["D1", "D2", "D3", "D4", "D5"],
        "country": ["ID", "ID", "ID", "US", "ID"],
        "amount_usd": [100, 110, 90, 5000, 50],
        "hour": [12, 13, 14, 2, 15],
        "is_new_beneficiary": [0, 0, 0, 1, 0],
        "is_cross_border": [0, 0, 0, 1, 0],
        "transactions_last_60m": [1, 1, 1, 15, 1],
    })

    scored = score_transactions(build_features(data))
    risky = scored.loc[scored["transaction_id"] == "T4", "alert_score"].item()
    normal = scored.loc[scored["transaction_id"] == "T1", "alert_score"].item()

    assert risky > normal
    assert risky >= 50
