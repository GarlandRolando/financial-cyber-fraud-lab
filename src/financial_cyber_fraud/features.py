from __future__ import annotations

import numpy as np
import pandas as pd

from .validation import validate_transactions


def _robust_customer_amount_score(group: pd.Series) -> pd.Series:
    median = group.median()
    mad = np.median(np.abs(group - median))

    if mad == 0 or np.isnan(mad):
        return pd.Series(np.zeros(len(group)), index=group.index)

    return 0.6745 * (group - median) / mad


def build_features(transactions: pd.DataFrame) -> pd.DataFrame:
    """Create explainable fraud-risk features from transaction data."""
    validate_transactions(transactions)
    result = transactions.copy()

    result["amount_robust_z"] = (
        result.groupby("customer_id")["amount_usd"]
        .transform(_robust_customer_amount_score)
        .fillna(0.0)
    )

    result["is_odd_hour"] = (
        (result["hour"] <= 4) | (result["hour"] >= 23)
    ).astype(int)

    device_customer_count = (
        result.groupby("device_id")["customer_id"].nunique()
    )
    result["device_customer_count"] = (
        result["device_id"].map(device_customer_count).fillna(1).astype(int)
    )
    result["is_shared_device"] = (
        result["device_customer_count"] >= 4
    ).astype(int)

    beneficiary_customer_count = (
        result.groupby("beneficiary_id")["customer_id"].nunique()
    )
    result["beneficiary_customer_count"] = (
        result["beneficiary_id"]
        .map(beneficiary_customer_count)
        .fillna(1)
        .astype(int)
    )
    result["is_concentrated_beneficiary"] = (
        result["beneficiary_customer_count"] >= 8
    ).astype(int)

    result["high_velocity"] = (
        result["transactions_last_60m"] >= 8
    ).astype(int)

    return result
