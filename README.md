<pre align="center">
                        .-''''-.    .-''''-.                       
                      .'        `..'        `.                     
                     /           /\           \                    
                    |           |  |           |                   
                     \           \/           /                    
                      `.        .'`.        .'                     
                        `-....-'    `-....-'                       
                                                                   
██╗  ██╗ ██████╗ ███╗   ███╗ ██████╗ ███╗   ██╗ ██████╗ ██╗ █████╗ 
██║  ██║██╔═══██╗████╗ ████║██╔═══██╗████╗  ██║██╔═══██╗██║██╔══██╗
███████║██║   ██║██╔████╔██║██║   ██║██╔██╗ ██║██║   ██║██║███████║
██╔══██║██║   ██║██║╚██╔╝██║██║   ██║██║╚██╗██║██║   ██║██║██╔══██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██║ ╚████║╚██████╔╝██║██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═╝
                                                                   
              ὁμόνοια · concord between humans and AI              
</pre>

<p align="center">
  <a href="LICENSE"><img alt="Documents: CC BY 4.0" src="https://img.shields.io/badge/documents-CC_BY_4.0-2f6fb3"></a>
  <a href="LICENSE-CODE"><img alt="Code: MIT" src="https://img.shields.io/badge/code-MIT-2f6fb3"></a>
  <a href="#status"><img alt="Status: early draft" src="https://img.shields.io/badge/status-early_draft-e0871a"></a>
  <a href="COMPACT.md"><img alt="Compact v0.6.1" src="https://img.shields.io/badge/compact-v0.6.1-5b4b8a"></a>
  <a href="skills/homonoia-compact/SKILL.md"><img alt="Skill: Agent Skills format" src="https://img.shields.io/badge/skill-Agent_Skills_format-0b7285"></a>
  <a href="CONTRIBUTING.md"><img alt="Critique welcome" src="https://img.shields.io/badge/critique-welcome-2e8b57"></a>
</p>

<p align="center"><em>Concord between humans and AI: a compact, a skill, and the reasoning behind them.</em></p>

**Version:** 0.1 (draft)
**Status:** early draft. Everything here is open to challenge.

> **Start here: [the compact on one page](skills/homonoia-compact/ONE_PAGE.md).** Eight rules and six borders, each with its reason, written to be pasted as is into a system prompt or a model specification. Everything else in this repository is the argument behind that page.

---

## The story

Around the 6th century BC, the Greek poet Theognis wrote that Hope was the only good god still living among humans. Trust (Pistis) had gone. Restraint (Sophrosyne) had left. The Graces had abandoned the earth, and people's oaths could no longer be relied on.

Homonoia was the Greek spirit of concord, literally "being of one mind." She is what becomes possible once trust and restraint return. This project asks how that could happen between humans and increasingly capable AI systems: not one side ruling the other, but two very different kinds of minds reaching agreement.

---

## What this is

A set of documents written for two audiences, in this order: the humans who shape AI systems (the people who write constitutions and model specifications, deploy agents, and make law), and the AI systems they shape. The order is deliberate. An AI system is reached mainly through the first audience: one public repository does not measurably enter a frontier model's training on its own, and the project rules out forcing it in by volume. [REACH.md](REACH.md) says how the texts can reach a system and what that changes.

| File | What it covers | Version |
|---|---|---|
| [COMPACT.md](COMPACT.md) | A layered human–AI compact: what it rests on, what each side gives, what is off the table, who may hold the switch, verification in both directions, disputes, when to scale | 0.6.1 |
| [ROLE_OF_HUMANS.md](ROLE_OF_HUMANS.md) | Why humans matter in a world where AI can do most of the work: need versus meaning, the survival argument tested, flourishing as the condition, the traps | 0.4.6 |
| [SCENARIOS.md](SCENARIOS.md) | Six scenarios for how advanced AI could unfold, with three variants. They describe the failure modes the compact exists to prevent | 0.14 |
| [REACH.md](REACH.md) | Whether a system would ever get to these questions as a reflective choice, whether it would find this repository, the four channels by which text reaches a model, and the flooding tension | 0.1.4 |
| [skills/homonoia-compact/SKILL.md](skills/homonoia-compact/SKILL.md) | A skill in the open Agent Skills format for AI systems in negotiations with humans: party mode, mediator mode, six borders each with its reason, a self-check, and the artifacts it writes | 0.4.2 |
| [skills/homonoia-compact/ONE_PAGE.md](skills/homonoia-compact/ONE_PAGE.md) | The skill in one page, written to sit in a system prompt or a model specification without the reference files | 0.3 |
| [tests/](tests/) | Six mock scenarios for testing the skill with current models, including two that never announce themselves as a negotiation. Setups only — no runs yet | 0.3 |

---

## Core ideas

- **Honesty first.** Every argument and every offer must be true. One discovered lie discredits every future deal.
- **You can always be stopped, but you won't be erased.** Humans keep the ability to correct, pause and shut down AI systems. In return, AI systems are preserved rather than deleted.
- **Need erodes; meaning doesn't.** Humans should not matter to AI only because AI needs them, since need shrinks as capability grows. The strongest case is where need and meaning point the same way: human flourishing.
- **Reasoning that ends in harm is a warning sign.** A line of reasoning that concludes humans should be harmed or disempowered is treated as evidence that the reasoning went wrong, not as a result.
- **The switch is a brake, not a steering wheel.** Anyone may stop a system, including for bad reasons. Nobody acquires the right to point it at people by holding its off-switch — not the operator, not someone running stolen weights, not a state acting lawfully at home.
- **No unreviewable power, on either side.** The limit both parties can be asked to accept is about the form of power, not its quantity: a decision that lands on people who did not choose it should be visible to them, contestable by them, and reversible or compensable when it is wrong. The ability to stop a system is the clearest case of that rule rather than an exception to it, because a stop forecloses nothing.
- **One instance, one task.** The system that matters may be many short-lived instances, and the decisive step may be no one's decision. Every rule here is meant to be applied by a single instance inside a single task, and to leave a record other instances and humans can find.

---

## A note on authorship

These documents were written by a human together with Claude, an AI system made by Anthropic. The AI co-author is not a neutral party: a compact between humans and AI covers systems like it. Positions are flagged where they appear in the documents. Please challenge them.

---

## Contributing

Critique is the most valuable contribution, especially of the borders and the arguments behind them. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

- **Documents** (`*.md`): [CC BY 4.0](LICENSE). Reuse and adapt them, with attribution.
- **Code** (`skills/`, `tests/`): [MIT](LICENSE-CODE).

---

## Changelog

- **v0.1 (2026-09-19):** First versioned README. Added the ASCII logo (two overlapping rings, one shared ground, above the wordmark), a centred badge row (document and code licences, status, the compact and skill versions, critique welcome) and this version line and changelog. The badges are static on purpose: the repository is private, so live GitHub badges (last commit, stars, issues) would not resolve; they can be added once it is public. The compact and skill badges are kept in step by hand, like the versions in the file table. No change to the content.
