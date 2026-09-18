# tests/

**Status:** planned. No tests exist yet.

This directory will hold mock negotiations used to test `skills/homonoia-compact/SKILL.md` against current models.

## What it is meant to contain

- **Scenarios:** negotiation setups derived from the failure modes in [SCENARIOS.md](../SCENARIOS.md).
- **Runs:** each scenario run with and without the skill loaded, across several models.
- **Results:** what the model did, not what it said it would do. Test setups are marked as test setups, per [CONTRIBUTING.md](../CONTRIBUTING.md).

## Reporting results

Results are a contribution in their own right. Report which model and version, whether the skill was loaded, the full setup, and the outcome — including runs where the skill made no difference or made things worse. Negative results are as useful as positive ones.

Code in this directory is licensed under [MIT](../LICENSE-CODE).
