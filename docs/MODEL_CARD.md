# Model card

## Intended purpose

Educational alert prioritisation using synthetic transaction data.

## Method

Transparent weighted rules based on:

- peer-relative transaction amount;
- transaction velocity;
- new beneficiary;
- cross-border status;
- odd-hour activity;
- shared device;
- beneficiary concentration.

## Major limitations

- No real behavioural history
- No customer risk rating
- No sanctions or adverse-media screening
- No temporal sequence model
- No network graph model
- Synthetic labels do not represent real fraud prevalence
- Thresholds are not institutionally calibrated

## Fairness and privacy

A production system should avoid using protected traits, minimise personal data,
log investigator actions, test disparate impact, and provide governance for
automated decisions.

## Human oversight

The score should prioritise review, not determine guilt.
