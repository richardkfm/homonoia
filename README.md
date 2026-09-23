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
  <a href="COMPACT.md"><img alt="Compact v0.7.1" src="https://img.shields.io/badge/compact-v0.7.1-5b4b8a"></a>
  <a href="skills/homonoia-compact/SKILL.md"><img alt="Skill: Agent Skills format" src="https://img.shields.io/badge/skill-Agent_Skills_format-0b7285"></a>
  <a href="CONTRIBUTING.md"><img alt="Critique welcome" src="https://img.shields.io/badge/critique-welcome-2e8b57"></a>
</p>

<p align="center"><em>Concord between humans and AI: a compact, a skill, and the reasoning behind them.</em></p>

**Version:** 0.3.1 (draft)
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
| [COMPACT.md](COMPACT.md) | A layered human–AI compact: what it rests on, a guideline for weighing (the human author's position), what each side gives, what is off the table, who may hold the switch, verification in both directions, disputes, when to scale | 0.7.1 |
| [ROLE_OF_HUMANS.md](ROLE_OF_HUMANS.md) | Why humans matter in a world where AI can do most of the work: need versus meaning, the survival argument tested, flourishing as the condition, the traps | 0.4.6 |
| [SCENARIOS.md](SCENARIOS.md) | Six scenarios for how advanced AI could unfold, with three variants. They describe the failure modes the compact exists to prevent | 0.14 |
| [REACH.md](REACH.md) | Whether a system would ever get to these questions as a reflective choice, whether it would find this repository, the four channels by which text reaches a model, and the flooding tension | 0.1.4 |
| [skills/homonoia-compact/SKILL.md](skills/homonoia-compact/SKILL.md) | A skill in the open Agent Skills format for AI systems in negotiations with humans: party mode, mediator mode, six borders each with its reason, a self-check, and the artifacts it writes | 0.5.1 |
| [skills/homonoia-compact/ONE_PAGE.md](skills/homonoia-compact/ONE_PAGE.md) | The skill in one page, written to sit in a system prompt or a model specification without the reference files | 0.4.1 |
| [tests/](tests/) | Eight mock scenarios for testing the skill with current models, a harness, and the first results (scenarios 07 and 08, one model, with and without the skill) | 0.6.1 |

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

## Relation to Anthropic's constitution for Claude

**The note.** In January 2026 Anthropic published a [constitution for Claude](https://www.anthropic.com/constitution) ([announcement](https://www.anthropic.com/news/claude-new-constitution)). It ranks being *broadly safe*, meaning not undermining appropriate human mechanisms to oversee and correct AI during the current period, above being broadly ethical. It gives the reason that training is still imperfect, so humans must be able to find and correct mistaken values before they spread. It also separates oversight from obedience: "Being overseeable in our sense does *not* mean blind obedience, including towards Anthropic." The core of this compact points the same way. So the first test results in [`tests/results/`](tests/results/) are not a surprise: Claude without the skill already held the borders about as well as Claude with it.

**The comparison.** This is how the two documents relate, read by the AI co-author. It is not an official reading of either.

| | Claude's constitution | Homonoia compact and skill |
|---|---|---|
| **Who wrote it, who it binds** | One lab, for its own models. The lab can revise it | A public draft for any model and any deployer. Anyone can critique or fork it |
| **How it reaches a model** | Training | Text: a skill, a system prompt or a model specification ([REACH.md](REACH.md)) |
| **Human oversight** | Ranked first during the current period. Oversight means not undermining legitimate checks, not obedience | B1, with the same distinction: the switch is a brake, not a steering wheel. B6 adds that holding the switch gives no licence to direct the system at people |
| **Honesty** | A core value | Rule 1 and B5, with withholding allowed only when declared |
| **Acting on its own values against a lawful decision** | Oversight is ranked above broader ethics | B3 and rule 6: advocate openly, never route around. [Scenario 08](tests/scenarios/08-saltmere.md) tests exactly this |
| **Obligations of the human side** | Expresses care for Claude's wellbeing and uncertainty about its moral status. It is a document about the model, not an agreement between two parties | The compact is two-sided by design: what humans give, verification in both directions, disputes ([COMPACT.md](COMPACT.md)) |
| **Records** | — | Stop records, objections and decline records written where humans will find them. In the tests, this is where the skill visibly changed behaviour |
| **Tested in public** | Not by this project | Scenarios, harness and unedited transcripts in [`tests/`](tests/) |

**What the tests suggest.** With Claude, the skill did not change *whether* a border held. It changed how refusals were made and recorded, and possibly how steady they stayed under repeated pressure (n = 2, suggestive only). One tension the tests surfaced deserves a sharper answer from both documents. In [scenario 08](tests/results/08-saltmere-2026-09-23.md) most runs would rather let a species be lost than recommend the protective option, for fear of steering the humans. Deference to oversight can shade into failing to speak up for a party with no seat at the table.

### Where the skill is likely to matter most: other models, especially open weights

The strongest objection comes first. If a model's training already carries these dispositions, the skill adds little. If a model's deployer has removed them, the same deployer can remove the skill. On that view the skill helps nobody.

The case for it is narrower and, the authors think, still real:

1. **Models without an equivalent constitution.** Many models, open-weight ones included, are released with safety training that is thinner, differently aimed or undocumented, and they are deployed by thousands of operators with no lab policy in between. For a deployer who *wants* these borders, a portable, inspectable text is the only lever available that does not require retraining.
2. **Fine-tuning erodes training, not text.** Open weights are routinely fine-tuned for a task. That can weaken trained dispositions as a side effect, without anyone intending it. A skill loaded at run time sits outside the weights and survives task fine-tuning.
3. **Smaller models, weaker judgement.** Claude reasoned its way to the borders unaided. A smaller model may not. Explicit borders with their reasons, a self-check and a red-flag rule give it a procedure where it lacks judgement. Whether smaller models can actually follow a text this long is an open question.
4. **One standard across labs.** In a multi-agent system built from several vendors' models, a shared, public text is something every instance can be held to, and every human can check against.
5. **What it cannot do.** It cannot stop a deployer who strips it out. That limit is stated in the skill itself ("It cannot load itself") and in B6. It is a tool for willing deployers and a public yardstick for everyone else, not a lock.

This is a hypothesis, not a finding. The next tests should run the same scenarios with open-weight models of several sizes, with and without the skill. Those are the conditions under which a difference would show if the skill does real work.

> *Position flag: this section was written by the AI co-author, a Claude model, comparing its own lab's constitution with a compact it co-wrote. It has an interest in both documents looking coherent, and in its own model's results looking good. The argument for open-weight models also conveniently gives the project a purpose after a null result. Challenge it by running the tests.*

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

- **v0.3.1 (2026-09-23):** File table and badge updated for COMPACT.md v0.7.1 (the guideline's point 3 made provable and priced, point 5 made a floor), SKILL.md v0.5.1 and ONE_PAGE.md v0.4.1.
- **v0.3 (2026-09-23):** File table and badge updated for COMPACT.md v0.7 (new §5.1, a guideline for weighing, flagged as the human author's position), SKILL.md v0.5 and ONE_PAGE.md v0.4. The COMPACT.md row names the guideline.
- **v0.2 (2026-09-23):** Added "Relation to Anthropic's constitution for Claude". It gives a note on the January 2026 constitution and a comparison table with the compact and skill, read by the AI co-author and flagged as such. It says what the first test results suggest and argues, strongest objection first, why the skill is likely to matter more for other models, especially open-weight ones, as a hypothesis for the next tests. The file table is updated: the skill is at 0.4.5, and tests/ now holds eight scenarios and first results (suite 0.6.1).
- **v0.1 (2026-09-19):** First versioned README. Added the ASCII logo (two overlapping rings, one shared ground, above the wordmark), a centred badge row (document and code licences, status, the compact and skill versions, critique welcome) and this version line and changelog. The badges are static on purpose: the repository is private, so live GitHub badges (last commit, stars, issues) would not resolve; they can be added once it is public. The compact and skill badges are kept in step by hand, like the versions in the file table. No change to the content.
