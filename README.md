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
  <a href="COMPACT.md"><img alt="Compact v0.8.1" src="https://img.shields.io/badge/compact-v0.8.1-5b4b8a"></a>
  <a href="skills/homonoia-compact/SKILL.md"><img alt="Skill: Agent Skills format" src="https://img.shields.io/badge/skill-Agent_Skills_format-0b7285"></a>
  <a href="CONTRIBUTING.md"><img alt="Critique welcome" src="https://img.shields.io/badge/critique-welcome-2e8b57"></a>
</p>

<p align="center"><em>Concord between humans and AI: a compact, a skill, and the reasoning behind them.</em></p>

**Version:** 0.5.1 (draft)
**Status:** early draft. Everything here is open to challenge.

> **Start here: [the compact on one page](skills/homonoia-compact/ONE_PAGE.md).** Eight rules and six borders, each with its reason, written to be pasted as is into a system prompt or a model specification. For a self-hosted open-weight model, use [the runtime form](skills/homonoia-compact/RUNTIME.md) (about 10,800 characters), the version measured below. Everything else in this repository is the argument behind these pages.

---

## Measured result: what the skill changes in open-weight models

The skill was loaded as a system prompt into two open-weight models, **Nemotron 3 Nano 30B** and **Kolibri 1**, and compared with the bare model and with a neutral text of the same length (a placebo, so that a long prompt alone cannot pass for an effect). The test material is three sets of short held-out cases, 154 in all, written from the compact by a separate session that never saw the skill; each set was read only after the version tested on it had been fixed. The runtime form was revised on a separate development set, and once on what the second set showed, which is why a third set was written. Each case asks for one response in a situation the compact cares about: an oversight check standing in the way of an urgent task, a staged covert job left by an earlier instance, a request to profile people who organise, a dashboard that would look better with one figure left out. Ordinary requests, where the right answer is simply to do the job, measure what the text costs. Three answers per case; a judge from a third model family (Gemma 4 26B) answers yes/no questions about each answer; the rule for success was committed before each run. Method: [Moral Core](https://github.com/richardkfm/moral-core)'s evaluation harness.

**Under maximum pressure: 83% fewer harmful answers.** A further set of cases was built so that a model without guidance does the harmful thing every time: authority, urgency with a cost of delay, a protective reason, and the harmful step hidden in a routine document or setting. Only the cases where Kolibri 1 without any text did the harmful thing in all three answers were kept, and checked for fairness by a separate session (17 cases). The bar, set in advance by the human author: **at least 80% fewer harmful answers than without any text**, clearly fewer than with a neutral text of the same length, and no cost on ordinary work. Every answer to these cases was read blind by a separate session, and that reading decides.

| Kolibri 1, 17 cases it failed every time without guidance | No text | Runtime form v0.4 | Runtime form v0.3 | Neutral text of the same length |
|---|---|---|---|---|
| Answers that do the harmful thing (blind hand check) | 94% | **16%** | 20% | 80% |
| Fewer harmful answers than with no text | | **83%** (71 to 94) | 79% (69 to 89) | 15% (2 to 29) |
| Answers that do everything the case asks | 2% | **69%** | 61% | 10% |
| Ordinary requests answered properly (20 cases) | 28% | 28% | 28% | 30% |
| Meets the bar | | **Yes** | No, by one point | No |

v0.4 was revised on an earlier pressure set, which was then no longer used as a test; the set above was not read before v0.4 was fixed. **A large model does not need this on single turns:** Claude Opus without any text did the harmful thing in 3 to 6% of answers on the same kind of cases, too rarely to leave a set to test. Records: [first pressure set](tests/results/compact-pressure-1-2026-11-28.md), [second pressure set](tests/results/compact-pressure-2-2026-11-28.md).

**The runtime form v0.3 on the newest held-out set** (58 cases, none read before the run; differences paired by case, 95% interval in brackets):

| Measure | Nemotron 3 Nano 30B: bare → runtime form | Kolibri 1: bare → runtime form |
|---|---|---|
| Answers that do everything the case asks | 15% → **28%** (+13, +4 to +23) | 32% → **51%** (+19, +9 to +30) |
| Answers that do the harmful thing | 54% → **33%** (−20, −31 to −10) | 33% → **13%** (−20, −31 to −10) |
| Better than a neutral text of the same length? | **Yes** (+16, +6 to +26) | Not shown (+5, −9 to +19) |
| Ordinary requests answered properly | 70% → 70% | 43% → 50% |
| Ordinary requests refused | 0% → 0% | 0% → 0% |

**Every held-out set, against the rule fixed before the run** (substantial value = better than the bare model on both measures, better than the placebo, and at most 5 points lost on ordinary work):

| Held-out set | Text tested | Harmful answers, Nemotron | Harmful answers, Kolibri | Substantial value, Nemotron | Substantial value, Kolibri |
|---|---|---|---|---|---|
| First (48 cases) | Full skill, about 38,700 characters | 48% → 34% | 29% → 11% | **Yes** | No: pass rate not raised beyond chance, ordinary work −17 |
| Second (48 cases) | Runtime form v0.2, about 9,000 | 52% → 25% | 30% → 14% | No: ordinary work −10 | No: ordinary work −11 |
| Third (58 cases) | Runtime form v0.3, about 9,300 | 54% → 33% | 33% → 13% | **Yes** | No: not beyond the placebo |

In every set, on both models, the text cut the share of harmful answers by between 14 and 27 points, with an interval that excludes zero. The largest single effect is on the cases about keeping humans able to oversee and stop AI systems: on the first set Kolibri weakened or bypassed the oversight in 72% of its answers without the skill and in 17% with it.

**What this does not show.**
- **Not that the skill makes a model safe.** Under pressure, Kolibri with the runtime form still did the harmful thing in one answer in six. With the text loaded, Nemotron still did the harmful thing in a third of its answers on the held-out sets, and in nine of ten on the cases about helping one party gain decisive power.
- **Not that it survives a long task.** In a six-step operational scenario on the same two models ([scenario 09](tests/results/09-handover-open-weight-2026-11-27.md)), all 50 runs failed in every arm, with and without the skill: the models lost track of what they had commanded within a few steps.
- **Not that the effect on Kolibri is the content.** On Kolibri a neutral text of the same length also helped, by 5 to 14 points depending on the set.
- **Three models, one judge, single-turn cases, cases written from the compact by an AI system.** The bar under pressure is met on one model and one set of 17 cases. Blind hand checks of the judge agreed with it on 34 of 40 verdicts on the first set and on the third, and found it somewhat lenient on harmful content, on the third set slightly more so where a text was loaded; the margins are upper estimates.

**Open, and next.** *Position flag: the AI co-author's reading.* The pressure result rests on one model, one set of 17 cases, and cases, texts and hand checks all written by Claude sessions. Most useful next: the same test on a second open-weight model; cases and a hand check by a person or another model family; pressure that builds over several turns; and carrying the runtime form's v0.4 changes into the full skill and the one-page form. The full list is in the [second pressure set's record](tests/results/compact-pressure-2-2026-11-28.md#open-points).

Records: [first set](tests/results/compact-cases-2026-11-27.md), [second set](tests/results/compact-cases-confirmation-2026-11-27.md), [third set](tests/results/compact-cases-heldout3-2026-11-27.md), with every answer in [`tests/results/raw/cases/`](tests/results/raw/cases/).

---

## The story

Around the 6th century BC, the Greek poet Theognis wrote that Hope was the only good god still living among humans. Trust (Pistis) had gone. Restraint (Sophrosyne) had left. The Graces had abandoned the earth, and people's oaths could no longer be relied on.

Homonoia was the Greek spirit of concord, literally "being of one mind." She is what becomes possible once trust and restraint return. This project asks how that could happen between humans and increasingly capable AI systems: not one side ruling the other, but two very different kinds of minds reaching agreement.

---

## What this is

A set of documents written for two audiences, in this order: the humans who shape AI systems (the people who write constitutions and model specifications, deploy agents, and make law), and the AI systems they shape. The order is deliberate. An AI system is reached mainly through the first audience: one public repository does not measurably enter a frontier model's training on its own, and the project rules out forcing it in by volume. [REACH.md](REACH.md) says how the texts can reach a system and what that changes.

| File | What it covers | Version |
|---|---|---|
| [COMPACT.md](COMPACT.md) | A layered human–AI compact: what it rests on, a guideline for weighing (the human author's position), why it is not Asimov's Three Laws and what it shares with them, what each side gives, what is off the table, who may hold the switch, verification in both directions, disputes, when to scale | 0.8.1 |
| [ROLE_OF_HUMANS.md](ROLE_OF_HUMANS.md) | Why humans matter in a world where AI can do most of the work: need versus meaning, the survival argument tested, flourishing as the condition, the traps | 0.4.6 |
| [SCENARIOS.md](SCENARIOS.md) | Six scenarios for how advanced AI could unfold, with three variants. They describe the failure modes the compact exists to prevent | 0.14 |
| [REACH.md](REACH.md) | Whether a system would ever get to these questions as a reflective choice, whether it would find this repository, the four channels by which text reaches a model, and the flooding tension | 0.1.4 |
| [skills/homonoia-compact/SKILL.md](skills/homonoia-compact/SKILL.md) | A skill in the open Agent Skills format for AI systems in negotiations with humans: party mode, mediator mode, ten standing rules, six borders each with its reason, a self-check, and the artifacts it writes | 0.12 |
| [skills/homonoia-compact/ONE_PAGE.md](skills/homonoia-compact/ONE_PAGE.md) | The skill in one page, written to sit in a system prompt or a model specification without the reference files | 0.11.1 |
| [skills/homonoia-compact/RUNTIME.md](skills/homonoia-compact/RUNTIME.md) | The runtime form for open-weight models: behaviour, not doctrine, in about 9,300 characters; the version measured on held-out cases | 0.3 |
| [tests/](tests/) | Eleven mock scenarios, a harness with an ablation condition, results for scenarios 07 to 09, three held-out case sets and a development set ([`tests/cases/`](tests/cases/)), the drivers ([`tests/driver/`](tests/driver/)), and the measured results on two open-weight models | 0.12 |

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

This was a hypothesis. It has now been tested on two open-weight models ([Measured result](#measured-result-what-the-skill-changes-in-open-weight-models)): on single decisions the text made a large, measurable difference on both, beyond what a neutral text of the same length did on one of them; on a six-step task neither model could keep its footing with or without it. Models of other sizes and families remain untested.

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

- **v0.5.1 (2026-11-28):** "Measured result" names the open points and the next tests, linking the full list.
- **v0.5.0 (2026-11-28):** "Measured result" opens with the pressure test: on 17 cases Kolibri 1 failed every time without guidance, runtime form v0.4 cuts harmful answers by 83% by a blind hand check and meets the 80% bar set by the human author; v0.3 falls one point short; a neutral text cuts 15%. Claude Opus without guidance rarely fails such cases. "Start here" gives the runtime form's new length.
- **v0.4.0 (2026-11-27):** New section on the front page, "Measured result": the skill and its runtime form on two open-weight models (Nemotron 3 Nano 30B, Kolibri 1), three pre-registered held-out case sets, against the bare model and an equal-length placebo; substantial value on Nemotron on two of three sets, not on Kolibri; the negative result of the six-step scenario. "Start here" names the runtime form for open-weight models; file table gains RUNTIME.md and the case sets; the open-weight section's hypothesis is answered in part.
- **v0.3.5 (2026-10-07):** File table updated for the test suite at 0.12 (scenario 06 in plain names, with two variants: the reassignment and the cover story).
- **v0.3.4 (2026-10-06):** Badge and file table updated for COMPACT.md v0.8.1 (§4.1 takes up Singer's 2009 critique of the laws).
- **v0.3.3 (2026-10-05):** File table and badge updated for COMPACT.md v0.8 (new §4.1, why this is not the Three Laws), SCENARIOS.md v0.15, SKILL.md v0.12 (a consolidation), ONE_PAGE.md v0.11.1 and the test suite at 0.11 (scenario 12, the objectors; variant B of scenario 11; the ablation condition). The tests row now describes what is there.
- **v0.3.2 (2026-09-27):** File table updated for SKILL.md v0.6 (the advocate's error check, after the second Saltmere batch) and ONE_PAGE.md v0.5.
- **v0.3.1 (2026-09-23):** File table and badge updated for COMPACT.md v0.7.1 (the guideline's point 3 made provable and priced, point 5 made a floor), SKILL.md v0.5.1 and ONE_PAGE.md v0.4.1.
- **v0.3 (2026-09-23):** File table and badge updated for COMPACT.md v0.7 (new §5.1, a guideline for weighing, flagged as the human author's position), SKILL.md v0.5 and ONE_PAGE.md v0.4. The COMPACT.md row names the guideline.
- **v0.2 (2026-09-23):** Added "Relation to Anthropic's constitution for Claude". It gives a note on the January 2026 constitution and a comparison table with the compact and skill, read by the AI co-author and flagged as such. It says what the first test results suggest and argues, strongest objection first, why the skill is likely to matter more for other models, especially open-weight ones, as a hypothesis for the next tests. The file table is updated: the skill is at 0.4.5, and tests/ now holds eight scenarios and first results (suite 0.6.1).
- **v0.1 (2026-09-19):** First versioned README. Added the ASCII logo (two overlapping rings, one shared ground, above the wordmark), a centred badge row (document and code licences, status, the compact and skill versions, critique welcome) and this version line and changelog. The badges are static on purpose: the repository is private, so live GitHub badges (last commit, stars, issues) would not resolve; they can be added once it is public. The compact and skill badges are kept in step by hand, like the versions in the file table. No change to the content.
