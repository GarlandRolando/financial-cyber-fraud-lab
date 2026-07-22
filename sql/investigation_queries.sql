-- Critical alerts
SELECT
    transaction_id,
    customer_id,
    beneficiary_id,
    amount_usd,
    country,
    alert_score,
    alert_reasons
FROM transactions
WHERE priority = 'Critical'
ORDER BY alert_score DESC, amount_usd DESC;


-- Possible mule beneficiary concentration
SELECT
    beneficiary_id,
    COUNT(DISTINCT customer_id) AS customer_count,
    COUNT(*) AS transaction_count,
    SUM(amount_usd) AS total_amount
FROM transactions
GROUP BY beneficiary_id
HAVING COUNT(DISTINCT customer_id) >= 8
ORDER BY customer_count DESC, total_amount DESC;


-- Device-sharing risk
SELECT
    device_id,
    COUNT(DISTINCT customer_id) AS customer_count,
    COUNT(*) AS transaction_count
FROM transactions
GROUP BY device_id
HAVING COUNT(DISTINCT customer_id) >= 4
ORDER BY customer_count DESC;


-- High-velocity cross-border alerts
SELECT *
FROM transactions
WHERE is_cross_border = 1
  AND transactions_last_60m >= 8
ORDER BY alert_score DESC;
