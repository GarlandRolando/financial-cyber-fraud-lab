from pathlib import Path

import pandas as pd
import streamlit as st

from financial_cyber_fraud.features import build_features
from financial_cyber_fraud.metrics import alert_summary, evaluate_synthetic_labels
from financial_cyber_fraud.scoring import score_transactions


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "synthetic_transactions.csv"

st.set_page_config(
    page_title="Financial Cyber-Fraud Lab",
    page_icon="🛡️",
    layout="wide",
)

st.title("Financial Cyber-Fraud Lab")
st.caption(
    "Explainable transaction monitoring for cyber-enabled fraud and financial crime analytics."
)

uploaded = st.sidebar.file_uploader("Optional CSV upload", type=["csv"])
if uploaded is None:
    transactions = pd.read_csv(DATA_PATH)
    st.sidebar.info("Using the synthetic demonstration dataset.")
else:
    transactions = pd.read_csv(uploaded)

try:
    features = build_features(transactions)
    scored = score_transactions(features)
except ValueError as exc:
    st.error(str(exc))
    st.stop()

summary = alert_summary(scored)
c1, c2, c3 = st.columns(3)
c1.metric("Transactions", f"{summary['transactions']:,}")
c2.metric("High or critical", f"{summary['high_or_critical']:,}")
c3.metric("Alert rate", f"{summary['high_or_critical_rate']:.1%}")

priority_filter = st.multiselect(
    "Priority",
    options=["Critical", "High", "Review", "Low"],
    default=["Critical", "High"],
)

filtered = scored[scored["priority"].isin(priority_filter)].copy()

st.subheader("Investigation queue")
columns = [
    "transaction_id",
    "customer_id",
    "beneficiary_id",
    "amount_usd",
    "country",
    "hour",
    "alert_score",
    "priority",
    "alert_reasons",
]
st.dataframe(
    filtered[columns].style.format({
        "amount_usd": "${:,.2f}",
        "alert_score": "{:.1f}",
    }),
    use_container_width=True,
)

st.subheader("Risk distribution")
distribution = (
    scored["priority"]
    .value_counts()
    .reindex(["Critical", "High", "Review", "Low"])
    .fillna(0)
)
st.bar_chart(distribution)

if "label_synthetic_fraud" in scored.columns:
    st.subheader("Synthetic validation")
    threshold = st.slider("Alert threshold", 10, 90, 50, 5)
    evaluation = evaluate_synthetic_labels(scored, threshold=threshold)

    e1, e2, e3, e4 = st.columns(4)
    e1.metric("Precision", f"{evaluation['precision']:.1%}")
    e2.metric("Recall", f"{evaluation['recall']:.1%}")
    e3.metric("False positives", evaluation["false_positives"])
    e4.metric("False negatives", evaluation["false_negatives"])

st.caption(
    "Educational project using synthetic data. Real investigations require "
    "validated controls, privacy safeguards, legal review, and human judgement."
)
