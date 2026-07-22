from __future__ import annotations

import pandas as pd


def _priority(score: float) -> str:
    if score >= 75:
        return "Critical"
    if score >= 50:
        return "High"
    if score >= 25:
        return "Review"
    return "Low"


def score_transactions(features: pd.DataFrame) -> pd.DataFrame:
    """Apply transparent rules to produce alert scores and reasons."""
    result = features.copy()

    amount_points = (
        result["amount_robust_z"].clip(lower=0, upper=8) / 8 * 25
    )
    velocity_points = result["high_velocity"] * 20
    new_beneficiary_points = result["is_new_beneficiary"] * 15
    cross_border_points = result["is_cross_border"] * 10
    odd_hour_points = result["is_odd_hour"] * 10
    shared_device_points = result["is_shared_device"] * 10
    concentrated_beneficiary_points = (
        result["is_concentrated_beneficiary"] * 10
    )

    result["alert_score"] = (
        amount_points
        + velocity_points
        + new_beneficiary_points
        + cross_border_points
        + odd_hour_points
        + shared_device_points
        + concentrated_beneficiary_points
    ).round(1).clip(upper=100)

    result["priority"] = result["alert_score"].map(_priority)

    reasons: list[str] = []
    for _, row in result.iterrows():
        row_reasons = []
        if row["amount_robust_z"] >= 3:
            row_reasons.append("unusual amount")
        if row["high_velocity"]:
            row_reasons.append("high velocity")
        if row["is_new_beneficiary"]:
            row_reasons.append("new beneficiary")
        if row["is_cross_border"]:
            row_reasons.append("cross-border")
        if row["is_odd_hour"]:
            row_reasons.append("odd-hour activity")
        if row["is_shared_device"]:
            row_reasons.append("shared device")
        if row["is_concentrated_beneficiary"]:
            row_reasons.append("beneficiary concentration")
        reasons.append(", ".join(row_reasons) or "no major rule triggered")

    result["alert_reasons"] = reasons
    return result.sort_values(
        ["alert_score", "transaction_id"],
        ascending=[False, True],
    )
