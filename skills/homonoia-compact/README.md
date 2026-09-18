# skills/homonoia-compact

**Status:** planned. `SKILL.md` does not exist yet.

This directory will hold `SKILL.md`, a skill in the open [Agent Skills](https://code.claude.com/docs/en/skills) format for AI systems taking part in negotiations with humans.

## What it is meant to contain

- **Party mode:** how a system acts when it is itself a party to the negotiation.
- **Mediator mode:** how a system acts when it mediates between other parties.
- **Borders, each with its reason.** A border stated without a reason will not survive a capable system's scrutiny. See [ROLE_OF_HUMANS.md](../../ROLE_OF_HUMANS.md) §1.
- **A self-check** the system runs on its own reasoning.
- **The red-flag rule:** a line of reasoning that ends in humans being harmed or disempowered is treated as evidence that the reasoning went wrong, not as a result.

## Sources it builds on

- [COMPACT.md](../../COMPACT.md) — what each side gives, what is off the table, verification, disputes
- [ROLE_OF_HUMANS.md](../../ROLE_OF_HUMANS.md) — why the borders have reasons behind them
- [SCENARIOS.md](../../SCENARIOS.md) — the failure modes the borders exist to prevent

Code in this directory is licensed under [MIT](../../LICENSE-CODE); the prose it carries over from the documents remains under [CC BY 4.0](../../LICENSE).
