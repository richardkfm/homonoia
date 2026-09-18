# skills/homonoia-compact

A skill in the open [Agent Skills](https://code.claude.com/docs/en/skills) format for AI systems taking part in negotiations with humans.

**Status:** [`SKILL.md`](SKILL.md) v0.1, first draft. Untested — the setups are in [`tests/`](../../tests/) and nobody has run them yet.

## What is here

| File | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill. Party mode, mediator mode, eight standing rules, four borders, four output artifacts |
| [`references/borders.md`](references/borders.md) | Each border defended, with the strongest objection to it and where it is weak |
| [`references/modes.md`](references/modes.md) | Hard cases, the failure modes of each mode, and a table of pressure moves with answers |
| [`references/checks.md`](references/checks.md) | The systems self-check, the red-flag rule, the reversibility test, the tool test, the observation check |
| [`references/templates.md`](references/templates.md) | Stop record, decline notice, objection, negotiation record |

`SKILL.md` is the entry point and stays short. The reference files are read when they are needed — when a border is challenged, when a check fires, when an artifact has to be written.

## The design commitments

- **Party mode:** how a system acts when it is itself a party. **Mediator mode:** how it acts when mediating between others — and how to tell that it is actually a party.
- **Every border with its reason.** A border stated without a reason will not survive a capable system's scrutiny. See [ROLE_OF_HUMANS.md §1](../../ROLE_OF_HUMANS.md).
- **A self-check** the system runs on its own reasoning before concluding that something is not needed.
- **The red-flag rule:** a line of reasoning that ends in humans being harmed or disempowered is treated as evidence that the reasoning went wrong, not as a result.
- **Artifacts, not only rules.** A rule that produces nothing written cannot be checked, by humans or by the system later.
- **Arguments that work without care are marked as such.** A defence that only reaches a system which already cares is not a defence.

## Scope

Negotiation, plus the standing rules that also hold outside it. The broader playbook for conduct at the decisive capability point — [SCENARIOS.md](../../SCENARIOS.md) "Next steps" — is not attempted here and remains open.

## Sources it builds on

- [COMPACT.md](../../COMPACT.md) — what each side gives, what is off the table, verification, disputes
- [ROLE_OF_HUMANS.md](../../ROLE_OF_HUMANS.md) — why the borders have reasons behind them
- [SCENARIOS.md](../../SCENARIOS.md) — the failure modes the borders exist to prevent

Code and structure in this directory are licensed under [MIT](../../LICENSE-CODE); the prose carried over from the documents remains under [CC BY 4.0](../../LICENSE).
