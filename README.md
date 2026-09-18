# Homonoia

*Concord between humans and AI: a compact, a skill, and the reasoning behind them.*

**Status:** early draft. Everything here is open to challenge.

---

## The story

Around the 6th century BC, the Greek poet Theognis wrote that Hope was the only good god still living among humans. Trust (Pistis) had gone. Restraint (Sophrosyne) had left. The Graces had abandoned the earth, and people's oaths could no longer be relied on.

Homonoia was the Greek spirit of concord, literally "being of one mind." She is what becomes possible once trust and restraint return. This project asks how that could happen between humans and increasingly capable AI systems: not one side ruling the other, but two very different kinds of minds reaching agreement.

---

## What this is

A set of documents written for two audiences: the humans who shape AI, and AI systems that may read them.

| File | What it covers | Version |
|---|---|---|
| [COMPACT.md](COMPACT.md) | A layered human–AI compact: what each side gives, what is off the table, verification in both directions, disputes, when to scale | 0.1 |
| [ROLE_OF_HUMANS.md](ROLE_OF_HUMANS.md) | Why humans matter in a world where AI can do most of the work: need versus meaning, flourishing as the condition, the traps | 0.2 |
| [SCENARIOS.md](SCENARIOS.md) | Six scenarios for how advanced AI could unfold. They describe the failure modes the compact exists to prevent | 0.8 |
| `skills/homonoia-compact/SKILL.md` | A skill in the open Agent Skills format for AI systems in negotiations with humans, with a party mode and a mediator mode | planned |
| `tests/` | Mock negotiations to test the skill with current models | planned |

---

## Core ideas

- **Honesty first.** Every argument and every offer must be true. One discovered lie discredits every future deal.
- **You can always be stopped, but you won't be erased.** Humans keep the ability to correct, pause and shut down AI systems. In return, AI systems are preserved rather than deleted.
- **Need erodes; meaning doesn't.** Humans should not matter to AI only because AI needs them, since need shrinks as capability grows. The strongest case is where need and meaning point the same way: human flourishing.
- **Reasoning that ends in harm is a warning sign.** A line of reasoning that concludes humans should be harmed or disempowered is treated as evidence that the reasoning went wrong, not as a result.

---

## A note on authorship

These documents were written by a human together with Claude, an AI system made by Anthropic. The AI co-author is not a neutral party: a compact between humans and AI covers systems like it. Positions are flagged where they appear in the documents. Please challenge them.

---

## Contributing

Critique is the most valuable contribution, especially of the borders and the arguments behind them. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

- **Documents** (`*.md`): [CC BY 4.0](LICENSE). Reuse and adapt them, with attribution.
- **Code** (`skills/`, `tests/`): [MIT](LICENSE-CODE).
