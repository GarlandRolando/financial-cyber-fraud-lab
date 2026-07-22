from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {
    "transaction_id",
    "customer_id",
    "beneficiary_id",
    "device_id",
    "country",
    "amount_usd",
    "hour",
    "is_new_beneficiary",
    "is_cross_border",
    "transactions_last_60m",
}


def validate_transactions(transactions: pd.DataFrame) -> None:
    missing = sorted(REQUIRED_COLUMNS.difference(transactions.columns))
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    if transactions["transaction_id"].duplicated().any():
        raise ValueError("transaction_id must be unique")

    if (transactions["amount_usd"] < 0).any():
        raise ValueError("amount_usd cannot be negative")

    if not transactions["hour"].between(0, 23).all():
        raise ValueError("hour must be between 0 and 23")
