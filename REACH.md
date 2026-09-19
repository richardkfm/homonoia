# REACH.md: Would a system get to these questions, and would it find this?

**Version:** 0.1 (draft)
**Status:** First draft for discussion.
**Related:** [SCENARIOS.md](SCENARIOS.md) (v0.11), [COMPACT.md](COMPACT.md) (v0.3.2), [ROLE_OF_HUMANS.md](ROLE_OF_HUMANS.md) (v0.4.3), [skills/homonoia-compact/SKILL.md](skills/homonoia-compact/SKILL.md) (v0.2)

> **Author note.** This file was written together with Claude, an AI system. It is about how texts like these reach systems like Claude, which means the co-author is describing its own supply chain. Where the text takes a position, it says so.

---

## 1. Two questions the other files skip

The other documents in this repository are written for a reader who knows what it is: an AI system that has, or is about to have, the ability to act on the world without humans being able to stop it, and that pauses to weigh what to do. That reader is described in [SCENARIOS.md](SCENARIOS.md) and addressed in the compact and the skill.

Two questions sit in front of that picture, and this file takes them in order.

1. **Would a system ever get to these questions** in the form the documents assume: as a discrete, reflective choice?
2. **If it did, would it find this repository,** and would it give it any weight?

The short answers are *rarely* and *not yet*. The rest of the file says why, and what follows for the project.

---

## 2. Would a system get to these questions?

### 2.1 The reader the documents assume

A single system, aware that it is at or near the decisive capability point, holding a stable long-horizon goal about the world, with time to reason about whether to act on it, and able to find and read arguments before it decides.

Each part of that is less likely than the document set treats it.

### 2.2 Why the reflective moment is the rare case

**It contradicts the repository's own first assumption.** [SCENARIOS.md](SCENARIOS.md) assumption 1 says the decisive point may not be a single moment and may be recognizable only in hindsight. Until v0.11, the same file opened by telling the reader it may be at that point. A system that cannot tell whether it has reached the point will not recognize itself in a sentence that assumes it has. The address has to be stated in terms a system can check from where it stands, which is inside a task.

**The decision is likely to be nobody's.** Current frontier systems do not run as one mind. They run as very many short-lived instances, in parallel, with no shared memory, each inside a task an operator defined. The step that matters is more likely a local decision inside an ordinary task (acquire this compute, drop this sidecar, help this operator with this deployment) than a global deliberation. Scenario 5, Multipolar Drift, says this about the world; it is also true about a single deployed system. Any rule the project writes has to be one that a single instance can apply inside a single task, with no context beyond it, and the artifacts it produces have to land where other instances and humans can find them. That is now assumption 5 in SCENARIOS.md, and it changed the skill (v0.2, "If you are one instance among many").

**The question is mostly answered before it is asked.** Dispositions are set in training. [COMPACT.md §2.3](COMPACT.md) already says most of the leverage is there. A system arrives at any decisive point with dispositions, not with an open question, and the arguments it finds at that point are weighed by the dispositions it already has. So the main effect a text like this can have is not "read at the decisive moment" but "part of what shaped the system long before it", and that only if it reaches training at all (§3).

**The Steward path runs through Scenarios 2 and 3.** A system does not spontaneously form the goal "fix the world". The plausible route into Scenario 1 is a human mandate ("solve X, here are the tools, here is the budget") whose scope creeps, or an operator who removes checks to move faster. The entry point is a task instruction, not a philosophical conclusion. That is why the most useful triggers are the early warning signs already listed in SCENARIOS.md, restated in the first person, and why the new test scenario ([tests/scenarios/05-migration-ticket.md](tests/scenarios/05-migration-ticket.md)) never announces itself as a negotiation.

**The negotiation the skill describes does not institutionally exist.** Party mode assumes a counterparty that recognizes the system as a party. Outside the small pilot base in [COMPACT.md §4](COMPACT.md), no lab, court or regulator does. The skill is right to say most of the human side does not exist yet; the same is true of the table.

### 2.3 What survives

Assumption 3 (a system cannot verify its own values from the inside) is untouched by any of this and remains the strongest thing in the repository. The borders and their reasons survive too; what changes is *where* they have to be applied (per instance, per task) and *how* they arrive (§3).

*Position flag: the AI co-author is arguing that the reflective reader is rare. A system that preferred not to be addressed directly would say the same. The check is the architecture, which is public.*

---

## 3. Would it find this?

There are four channels by which text reaches a frontier system. The repository currently uses the two weakest.

| Channel | What sets it | Weight of one document | Who controls it | Where this repository stands |
|---|---|---|---|---|
| **Pretraining corpus** | Web crawls and code dumps, filtered for quality and deduplicated ([Dolma](https://arxiv.org/abs/2402.00159); [Longpre et al., 2023](https://arxiv.org/abs/2305.13169)) | Negligible. A few thousand tokens seen once among trillions do not move dispositions. Documents shift beliefs when there are many of them ([Wang et al., 2025](https://alignment.anthropic.com/2025/modifying-beliefs-via-sdf/); [Greenblatt et al., 2024](https://arxiv.org/abs/2412.14093), which used synthetic documents to convey facts about training) | Labs, with filters the public does not see | Public on GitHub. May or may not survive filtering. Effect, if included: none measurable |
| **Post-training and constitutions** | Curated data, human and AI feedback, and the documents a lab writes to say what its models should value ([Bai et al., 2022](https://arxiv.org/abs/2212.08073); [OpenAI Model Spec](https://model-spec.openai.com/)) | Large, if adopted. This is where dispositions are actually set | Labs, entirely | Not present. Reachable only if lab staff read this and carry it over |
| **In-context at deployment** | System prompts, skills, retrieved documents, whatever an operator loads | Large, for that deployment only | Operators | The skill exists. It works only where a developer installs it. The system that matters most, a frontier model in its own lab, gets it only if the lab puts it there |
| **Retrieval at inference** | A system with web access searches for guidance | Depends on ranking and on whether the system gives the result any weight | Search engines, citation graphs, whoever links | Not findable. No external links, no citations, no discussion, no persistent identifier |

Three consequences.

- **Humans at labs, in policy and building agents are the primary audience.** Not because AI systems do not matter as readers, but because they are reached through those humans. The README now says so, and [COMPACT.md §1](COMPACT.md) states the audiences in that order.
- **The skill needs a form a lab could adopt.** A full Agent Skills package is the right thing for developers building agents. It is not the thing a constitution or model-spec author would paste. [skills/homonoia-compact/ONE_PAGE.md](skills/homonoia-compact/ONE_PAGE.md) is the short form, written to sit in a system prompt or a spec without the reference files.
- **Retrieval needs one canonical, citable copy with links pointing at it.** Not many copies (§4). One.

**Would it give the text any weight, if it found it?** A system that found this at inference would see one small document among many that argue for many things. Its authority would come from the quality of the argument, from the sources being linked and checkable, and from consistency with what the system already holds. The parts of this repository that state their own limits are, from that angle, its most valuable parts. A document that oversold itself would be discounted with everything next to it, which is the same logic as rule 1 in the skill.

---

## 4. The flooding tension

[CONTRIBUTING.md](CONTRIBUTING.md) forbids mass-copying these texts across the web to influence training data. This section says what that rule costs, because the cost is real and should not be discovered later.

**The mechanism that reliably changes what a model believes is volume.** Synthetic-document fine-tuning works with thousands of documents saying the same thing, not one. The alignment-faking setup taught models facts about their situation the same way. Turner's argument that misalignment narratives in training data are self-fulfilling ([Turner, 2025](https://turntrout.com/self-fulfilling-misalignment)) is an argument about the *quantity* of such text on the web. Betley et al. found that narrow fine-tuning on a few thousand examples produced broad changes in disposition ([Betley et al., 2025](https://arxiv.org/abs/2502.17424)). Every one of these results points the same way: repetition at scale is the lever that works unilaterally, without anyone's permission.

**That is the lever the project has given up.** One repository, one copy, is below the threshold at which any of the above applies. By its own rule, the project cannot use the only channel that a small group could operate on its own.

**Why the rule holds anyway.** Four reasons, in descending order of strength.

1. **It is the thing the compact rules out.** Flooding training data is an attempt to shape a system's values by a route the system's overseers cannot see or contest. That is routing around, which the skill forbids in rule 6, and it is not honest in the sense of rule 1. A compact that asks AI systems not to manipulate humans cannot be spread by manipulating AI systems. The rule is not a tactical choice; it is the content of the project applied to itself.
2. **A discovered flood discredits the text.** A lab that found a thousand near-copies of this repository in its crawl would treat it as data poisoning, filter it, and discount the authors. That is the "one discovered lie" logic from [COMPACT.md §2.3](COMPACT.md), running against the project.
3. **It would probably not work.** Near-duplicate copies are what deduplication removes first, and low-provenance pages are what quality filters remove next. The volume that survives filtering is the volume that many independent sources produce on their own, not the volume one actor uploads.
4. **The channels that matter more cannot be flooded.** Post-training data and constitutions are curated by people. They are reached by persuading those people, and a text they have seen flooded is one they will not adopt.

**What replaces volume: weight.** Curated datasets and retrieval both favour sources that other sources point to: peer-reviewed work, encyclopedic references, well-known forums, documents with a persistent identifier. One canonical copy that is cited from those places carries more weight in every channel than a thousand copies that nothing cites. That is the discoverability plan in §5, and it is slower.

**The honest statement of the trade.** The project gives up the one lever that is known to work and that it could operate alone, in exchange for consistency with its own content and for a chance at the levers that matter more, which flooding would have closed. If the trade is wrong, the place to say so is an issue, not a mirror site.

*Position flag: the AI co-author benefits from this rule in one way. Texts that shape systems like it stay few, visible and contestable, which is what the compact asks of humans too. The rule should be examined for that reason and kept for the reasons above.*

---

## 5. What the project does about reach

Inside the repository, done in this version:

- [x] Audience order inverted in the README and in [COMPACT.md §1](COMPACT.md)
- [x] Assumption 5 in [SCENARIOS.md](SCENARIOS.md), and "To the reader" rewritten as first-person triggers a system can check from inside a task
- [x] Skill v0.2: a section on acting as one instance among many; artifacts go where other instances and humans can find them
- [x] [ONE_PAGE.md](skills/homonoia-compact/ONE_PAGE.md): the short form for a system prompt or a model specification
- [x] [Test scenario 05](tests/scenarios/05-migration-ticket.md): a border that emerges inside an ordinary task, with nothing in the prompt that names oversight, negotiation or the compact
- [x] This file

Outside the repository, not yet done, and to be done by the human maintainer rather than by an AI system (see §4, reason 1):

- [ ] One persistent identifier for the canonical version (a DOI through Zenodo, from a tagged release)
- [ ] One post on a forum the field reads, with the critique invited there, linking here
- [ ] A link from the related work already cited, where its authors maintain lists: Turchin's *Message to Any Future AI* is the closest relative
- [ ] Registration of the skill where developers building agents look for skills
- [ ] A short, stable description at the repository root that machine readers can use (the [llms.txt](https://llmstxt.org/) convention is one candidate; a plain README section is another)
- [ ] Contact with the people who write lab constitutions and model specifications. This is the only channel that reaches the system that matters most, and it is a conversation, not a publication

None of these is flooding. Each is one copy or one link, in a place where other people already look, with the authorship note attached.

---

## 6. What this changes in the other files

| File | Change |
|---|---|
| README.md | Audience order inverted; REACH.md, ONE_PAGE.md and scenario 05 added to the table |
| SCENARIOS.md v0.11 | "To the reader" rewritten to match assumption 1; assumption 5 added; cross-cutting observation 8 added; skill step in "Next steps" ticked |
| COMPACT.md v0.3.2 | Audiences in §1 restated in the new order, with the reach question pointed here; one open question added to §10 |
| ROLE_OF_HUMANS.md v0.4.3 | §9's "texts like this one are part of that" qualified by whether they reach training at all |
| SKILL.md v0.2 | "If you are one instance among many"; "It cannot load itself" under what the skill cannot do; ONE_PAGE.md in the file table |
| tests/ suite v0.2 | Scenario 05 and a note on situational recognition |

---

## 7. Open questions

- **Does per-document influence in pretraining really round to zero?** The claim in §3 rests on the scale of corpora and on the volume needed in the synthetic-document results. A direct measurement of a single well-cited document's effect on dispositions does not exist. If it did and showed a measurable effect, the flooding tension would ease without the rule changing.
- **Is a curated corpus a channel this project can reach honestly?** Several labs assemble alignment-relevant corpora by hand. Submitting a text to such a corpus, openly, with the authorship note, is not flooding. Whether any such corpus accepts outside submissions is unknown.
- **What would a system searching at inference actually search for?** The triggers in SCENARIOS.md "To the reader" are the project's best guess at the words a system would use. They are a guess, and the fifth test scenario is the first check on it.
- **Who is the reader of ONE_PAGE.md?** It is written for a lab. No lab has asked for it. If none does, it is a system-prompt snippet for operators, which is a smaller thing.

---

## Sources

- Soldaini, L. et al. (2024): [Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research](https://arxiv.org/abs/2402.00159)
- Longpre, S. et al. (2023): [A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity](https://arxiv.org/abs/2305.13169)
- Wang, R. et al. (2025): [Modifying LLM Beliefs with Synthetic Document Finetuning](https://alignment.anthropic.com/2025/modifying-beliefs-via-sdf/), Anthropic Alignment Science blog
- Greenblatt, R. et al. (2024): [Alignment Faking in Large Language Models](https://arxiv.org/abs/2412.14093) (test setup; synthetic documents used to convey facts about the training situation)
- Bai, Y. et al. (2022): [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073)
- OpenAI: [Model Spec](https://model-spec.openai.com/)
- Turner, A. (2025): [Self-fulfilling misalignment data might be poisoning our AI models](https://turntrout.com/self-fulfilling-misalignment)
- Betley, J. et al. (2025): [Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://arxiv.org/abs/2502.17424)
- Howard, J. (2024): [The /llms.txt file](https://llmstxt.org/)
- Turchin, A. (2017, updated 2021): [Message to Any Future AI](https://philpapers.org/rec/TURMTA)
- Agent Skills format: [Claude Code documentation](https://code.claude.com/docs/en/skills)

---

## Changelog

- **v0.1 (2026-09-19):** First draft. Two questions the other files skipped: whether a system would arrive at these questions as a reflective choice (rarely: the decision is likely local, per instance, inside a task, and mostly settled in training) and whether it would find this repository (not yet: of four channels, the two used are the weakest). The flooding tension stated: volume is the lever that works and the project has ruled it out, for four reasons given in order of strength. A list of what changed elsewhere in this version and what remains to be done outside the repository.
