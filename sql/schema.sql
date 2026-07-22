CREATE TABLE transactions (
    transaction_id VARCHAR(40) PRIMARY KEY,
    customer_id VARCHAR(40) NOT NULL,
    beneficiary_id VARCHAR(40) NOT NULL,
    device_id VARCHAR(40) NOT NULL,
    country CHAR(2) NOT NULL,
    amount_usd DECIMAL(18, 2) NOT NULL,
    transaction_hour INTEGER NOT NULL,
    is_new_beneficiary INTEGER NOT NULL,
    is_cross_border INTEGER NOT NULL,
    transactions_last_60m INTEGER NOT NULL,
    alert_score DECIMAL(5, 2),
    priority VARCHAR(20),
    alert_reasons VARCHAR(500)
);
