import pandas as pd
import pytest

from financial_cyber_fraud.validation import validate_transactions


def test_duplicate_transaction_rejected():
    data = pd.DataFrame({
        "transaction_id": ["T1", "T1"],
        "customer_id": ["C1", "C2"],
        "beneficiary_id": ["B1", "B2"],
        "device_id": ["D1", "D2"],
        "country": ["ID", "SG"],
        "amount_usd": [10, 20],
        "hour": [10, 11],
        "is_new_beneficiary": [0, 1],
        "is_cross_border": [0, 1],
        "transactions_last_60m": [1, 2],
    })

    with pytest.raises(ValueError):
        validate_transactions(data)
