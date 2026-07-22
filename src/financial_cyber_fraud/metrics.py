from __future__ import annotations

import pandas as pd


def alert_summary(scored: pd.DataFrame) -> dict[str, float]:
    total = len(scored)
    high_or_critical = int(scored["priority"].isin(["High", "Critical"]).sum())
    return {
        "transactions": total,
        "high_or_critical": high_or_critical,
        "high_or_critical_rate": 0.0 if total == 0 else high_or_critical / total,
        "mean_score": 0.0 if total == 0 else float(scored["alert_score"].mean()),
    }


def evaluate_synthetic_labels(scored: pd.DataFrame, threshold: float = 50) -> dict[str, float]:
    if "label_synthetic_fraud" not in scored.columns:
        raise ValueError("Synthetic label column is unavailable")

    predicted = scored["alert_score"] >= threshold
    actual = scored["label_synthetic_fraud"] == 1

    tp = int((predicted & actual).sum())
    fp = int((predicted & ~actual).sum())
    fn = int((~predicted & actual).sum())

    precision = 0.0 if tp + fp == 0 else tp / (tp + fp)
    recall = 0.0 if tp + fn == 0 else tp / (tp + fn)

    return {
        "true_positives": tp,
        "false_positives": fp,
        "false_negatives": fn,
        "precision": precision,
        "recall": recall,
    }
