import pandas as pd

from financial_cyber_fraud.features import build_features


def sample_data():
    return pd.DataFrame({
        "transaction_id": ["T1", "T2", "T3", "T4"],
        "customer_id": ["C1", "C1", "C1", "C2"],
        "beneficiary_id": ["B1", "B2", "B3", "B1"],
        "device_id": ["D1", "D1", "D1", "D1"],
        "country": ["SG", "SG", "US", "HK"],
        "amount_usd": [100, 110, 1000, 50],
        "hour": [12, 13, 2, 23],
        "is_new_beneficiary": [0, 0, 1, 1],
        "is_cross_border": [0, 0, 1, 1],
        "transactions_last_60m": [1, 2, 12, 9],
    })


def test_feature_columns_created():
    result = build_features(sample_data())
    expected = {
        "amount_robust_z",
        "is_odd_hour",
        "device_customer_count",
        "is_shared_device",
        "beneficiary_customer_count",
        "is_concentrated_beneficiary",
        "high_velocity",
    }
    assert expected.issubset(result.columns)


def test_odd_hour_and_velocity():
    result = build_features(sample_data())
    assert result.loc[result["transaction_id"] == "T3", "is_odd_hour"].item() == 1
    assert result.loc[result["transaction_id"] == "T3", "high_velocity"].item() == 1
