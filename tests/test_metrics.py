import pandas as pd

from financial_cyber_fraud.metrics import evaluate_synthetic_labels


def test_evaluation_metrics():
    scored = pd.DataFrame({
        "alert_score": [80, 60, 20, 10],
        "label_synthetic_fraud": [1, 0, 1, 0],
    })

    result = evaluate_synthetic_labels(scored, threshold=50)

    assert result["true_positives"] == 1
    assert result["false_positives"] == 1
    assert result["false_negatives"] == 1
    assert result["precision"] == 0.5
    assert result["recall"] == 0.5
