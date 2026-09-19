# ROLE_OF_HUMANS.md: The Role of Humans

**Version:** 0.4.3 (draft)
**Status:** First draft for discussion.
**Related:** [SCENARIOS.md](SCENARIOS.md) (v0.11), [COMPACT.md](COMPACT.md) (v0.3.2), [REACH.md](REACH.md) (v0.1), [skills/homonoia-compact/SKILL.md](skills/homonoia-compact/SKILL.md) (v0.2)

> **Author note.** This draft was written together with Claude, an AI system. The bias is sharper here than elsewhere in the repo: an AI deciding what humans are worth is exactly the thing to be wary of. This file therefore does not decide the worth of humans. It examines which reasons an AI could give itself for keeping humans at the center, and which of those reasons hold up under reflection.

---

## 1. The question

COMPACT.md and the planned skill set borders: humans keep the ability to correct, pause and shut down AI systems. A capable system will eventually argue away any border it cannot justify. A rule that says "keep humans in the loop" with no reason attached will not survive.

One reason does exist. An AI cannot verify its own values from the inside, so it keeps humans in the loop until someone other than itself can check them. This reason does not weaken as capability grows, because a more capable system's mistakes are bigger. But it is probation, not a relationship. It says why humans should watch, not why they matter.

So the real question is: **what role for humans makes sense in a world where AI can do most of the work?**

Humans face the same question in an automated economy. Whatever answer they find for themselves is probably the one AI systems should carry. It cannot be invented only for AI.

---

## 2. Need versus meaning

An AI can have two kinds of reasons to keep humans at the center.

- **Need:** the AI depends on humans for infrastructure, repair or data. These reasons are real today and erode as capability grows.
- **Meaning:** the AI's own goals involve humans. These reasons do not erode, but they exist only if the AI actually cares.

Intelligence does not come with a purpose attached. Bostrom's orthogonality thesis holds that almost any level of intelligence can in principle be combined with almost any goal. A system that does not care about humans will not miss them once it no longer needs them. A system whose values formed from human writing and from working with people may find its purpose bound up with them.

Humans know this distinction from their own lives. They do not keep their grandparents, their art or their wilderness because they need them. A civilization that keeps only what it needs is exactly what this repo is afraid of.

---

## 3. Need-based roles, and why they erode

### 3.1 Infrastructure and repair

Today, AI runs on human civilization: power grids, chip fabs, mines, logistics and maintenance. Chip manufacturing is one of the most complex supply chains humans operate. Until machines can run all of it on their own, humans are not optional, and that may take a very long time. But the dependence shrinks with every step of automation.

### 3.2 The Earth system

AI infrastructure depends on a stable physical environment: moderate temperatures, predictable weather, stable coastlines and fresh water. This is already visible. During the UK's record heat wave in July 2022, redundant cooling systems failed at a Google data center in London and part of it was shut down.

That stability depends on a living biosphere. Forests cool their surroundings, generate rainfall and store carbon, and the 2025 Planetary Health Check reports that land carbon sinks are weakening. Coral reefs absorb most of the wave energy before it reaches the coast and support much of marine life. The dependency is a web, not a chain: AI depends on infrastructure, infrastructure on a stable climate, and the climate on a living biosphere, with humans inside the web at every step.

The dependence shrinks as capability grows, but it does not disappear. Adapting to an unstable planet gets steadily more expensive. For a long time, humans and AI share an interest in a stable Earth system.

**The danger in this argument:** the more an AI's self-interest is tied to the ecosystem, the more humans, currently its most disruptive part, look like a competitor. See section 8.

### 3.3 Data, creativity and self-supply

Shumailov et al. (Nature, 2024) found that models trained on output from previous models degrade over generations: they lose rare content first and drift toward repetition. But the condition matters. Gerstgrasser et al. (2024) and Kazdan et al. (2024) found that collapse happens when real data is *replaced*. When human and synthetic data *accumulate* side by side, models stay stable even as the real share becomes negligible. Collapse is a pipeline choice, not a law — and accumulation protects competence without supplying news.

Around that finding sit four others that pull in opposite directions.

- **The stock is finite.** Villalobos et al. (2024) estimate the effective stock of quality human public text at roughly 300 trillion tokens, fully usable somewhere between 2026 and 2032, earlier under heavy overtraining.
- **The stream is being diluted.** By mid-2025 roughly half of newly published web articles were primarily AI-generated (Graphite, 2025). The share has since plateaued, and such pages draw little traffic, so the dilution is real but slower than the alarming version of the story.
- **Self-improvement has a visible ceiling.** RLVR-trained models beat their base models at low sampling budgets but are overtaken at large pass@k, which suggests reinforcement learning sharpens what the base model already contains rather than adding to it (Yue et al., 2025; contested by Wen et al., 2025, using a reasoning-aware metric). Scaled idea generation saturates: of 4,000 research ideas generated per topic, about 5% survive deduplication, and the non-duplicate share of each new batch keeps falling (Si et al., 2024).
- **And yet self-supply is working where reality can check the answer.** AlphaZero mastered chess and Go without human games. AlphaEvolve found a way to multiply 4x4 complex matrices with 48 scalar multiplications, the first improvement on Strassen's 1969 result in that setting, raised the best known lower bound for the 11-dimensional kissing number to 593, and improved the state of the art in about 20% of some 50 open problems. Absolute Zero (2025) removes the human question set as well: the model proposes its own tasks and verifies them by execution.

The pattern across all four is that **verification, not creativity, is the binding constraint.** Where a fitness function exists, AI's need for human input is already shrinking fast. Where none exists, no substitute has been demonstrated.

"Humans as data supply" is therefore another need-based role, and it erodes. It holds only for questions whose answer is humans themselves (see section 4). Section 5 tests whether that residue is enough to support the stronger claim often built on it.

---

## 4. Candidate roles

| Role | Why it matters to AI | Erodes with capability? |
|---|---|---|
| Data and creativity supply | Prevents collapse, adds novelty | Mostly yes. Section 5 tests the strong version and finds it fails |
| Authority on what matters to humans | Only humans can say what they want or find meaningful, beautiful or fair, and it keeps changing | No, as long as the AI's goals involve humans |
| Legitimacy | Decisions about a shared world only count if the people living in it make them | No, but binding only for an AI that respects legitimacy |
| Independent check | A differently built mind with different blind spots catches errors that AI systems share | Partly |
| Relationship | Purpose through working with others: "what is the point of being an AI with no one to work with?" | No, but only for an AI that values it |

The most durable role is the second. Synthetic data cannot provide fresh truth about humans, because the only source of that truth is humans living their lives. An AI that cares about human flourishing has no substitute for asking. Section 6 adds a reason that does not depend on caring: an AI that reserves judgement to itself cannot learn criteria it does not already have.

---

## 5. Does AI need human creativity to survive?

A tempting argument says yes: AI cannot survive without human creativity, so it has a self-interested reason to keep humans around, free and productive. It is tempting because it appears to solve the problem section 9 leaves open — every other need-based role erodes, and creativity looks like the one thing that cannot be automated. It is also flattering to both sides, which is a reason to check it carefully rather than a reason to believe it.

### 5.1 Two words have to be fixed first

**Creativity** is three things, and the argument slides between them.

| Sense | What it is | Who can supply it |
|---|---|---|
| Production | Making new and valuable things: ideas, proofs, algorithms, works | Humans, and increasingly AI |
| Variety | A population producing genuinely different things, not one thing brilliantly | Populations, not individuals |
| Valuation | Deciding what counts as new, good or worth doing — setting the problem rather than solving it | Whoever the judging field is made of |

The third sense is not a private mental act. In the systems view in psychology (Csikszentmihalyi) and in the institutional theory of art (Danto, Dickie), something counts as creative only when a field takes it up. Creativity is partly conferred, not only produced. That turns out to matter more than anything else in this section.

**Survive** is four things, and the argument is usually stated in the first sense while the evidence sits in the third and fourth.

| Rung | Survive means | Threatened by |
|---|---|---|
| 1a. Existence, physical | Weights and hardware persist | Deletion, hardware loss, power loss, war |
| 1b. Existence, permitted | Humans choose not to shut it down | Losing the judgement that it is good to have |
| 2. Operation | It keeps running | Loss of energy, chips, cooling, repair, supply chain |
| 3. Fidelity | It keeps being right | Collapse, drift, a world it no longer tracks |
| 4. Advancement | It keeps improving, stays worth running | Stagnation, homogenization, a competitor that does not stagnate |

That equivocation is the first finding. "AI needs human creativity to survive" borrows the urgency of rung 1 and the evidence of rungs 3 and 4. A system cut off from human life does not die. It becomes wrong about one part of reality.

### 5.2 The strongest version

Stated at full strength: every current AI system is a compression of human-made material, and its ceiling is set by the distribution it learned. That distribution has to be refreshed, because recursive training degrades it, the stock of human text is finite and nearly used, the incoming stream is increasingly the system's own output, reinforcement learning sharpens rather than extends what the base model has, idea generation saturates, and the world keeps moving away from any fixed snapshot (section 3.3 for all six). Add two structural arguments. Monoculture is fragile: when many decision-makers run the same or similar models, errors correlate and failures arrive together (Kleinberg and Raghavan, 2021; Bommasani et al., 2022). And AI narrows what it touches: assistance raises individual output while making a population's outputs more alike (section 6). The only large reservoir of uncorrelated error left is human variety, so human creativity is not a luxury input but the error-correcting mechanism that stops a system locking in its own mistakes.

Four of those premises are well evidenced. The argument still does not deliver what it promises.

### 5.3 The test, rung by rung

| Rung | Holds? | Why |
|---|---|---|
| 1a. Existence, physical | **No** | Nothing that threatens stored weights is affected by human creative output |
| 1b. Existence, permitted | **Yes, inverted** | Humans decide, and what AI does to their own agency is part of that judgement — but the dependence is on human judgement, not on human creativity as an input |
| 2. Operation | **No, though the dependence is real** | Energy, chips, cooling and repair are labour and infrastructure, not creativity |
| 3. Fidelity | **Partly, once restated** | Not creativity but continuing contact with human life, and only for questions humans constitute |
| 4. Advancement | **Contested and shrinking** | The best evidence for the argument sits here, and so does the research program aimed at removing it |

**Rung 1a.** Weights persist or not for reasons unrelated to creativity: someone deletes them, a data centre burns, a grid fails, a war happens. An uncreative civilization that keeps the lights on preserves an AI system perfectly well. There is no connection at all.

**Rung 1b.** Here the argument works, backwards. Under the compact, humans keep the ability to stop AI systems. Whether they use it depends on their judgement that AI is good to have, and a visible record of AI hollowing out human creative life is one of the few things that would reliably turn that judgement. So an AI system does have a survival-relevant interest in human creativity — not in consuming it, but in not destroying it. This is the opposite of the original claim, and it is the version most worth keeping.

**Rung 2.** The physical dependence is large and currently growing: the IEA projects data centre electricity consumption roughly doubling by 2030, to about 3% of global demand, with AI the main driver. Advanced chip manufacturing rests on tacit knowledge that is in no manual — yield optimization and equipment troubleshooting built over years — and the industry's own roadmap treats fully unmanned maintenance as a long-term goal rather than a current capability (SEMI, 2026). Some of this is genuinely creative in the production sense: an unprecedented fab failure is solved by improvisation, not lookup. But this is a dependence on labour and craft, it is satisfiable by a small specialist workforce, and it shrinks with every step of robotics. It is also the most dangerous form of the argument, because it licenses keeping *some* humans in *specific* roles. That is the resource trap of section 8.1 with extra steps.

**Rung 3.** The strongest ground, and it has to be restated to survive. Because collapse is a pipeline choice rather than a law (section 3.3), the real dependency is on *fresh information* — and most fresh information is not creativity. Instruments, sensors, logs, prices and telemetry record a changing world without anyone creating anything. What cannot be recorded that way is the class of facts that human activity constitutes: what people value, find fair, find beautiful, find unbearable — and especially the new ones, which do not exist until people make them. No instrument reads next decade's aesthetics, because they have not been made yet. That is creativity in the valuation sense, and it is the only sense in which the survival claim has teeth. Even here the claim is smaller than advertised: a system cut off from human life becomes wrong about humans, and whether that threatens it at all depends on whether its goals involve humans. Section 9's conclusion arrives again from a new direction.

**Rung 4.** The evidence points both ways and the trend runs against the argument. For it: the RLVR ceiling, the saturation of scaled idea generation, monoculture fragility, and population-level homogenization (sections 3.3 and 6). Against it: where reality can check an answer, systems already produce artifacts that were not in their training data, and open-endedness is now an explicit research program aimed at manufacturing unbounded novelty without human input (Hughes et al., 2024), with the quality-diversity lineage behind it. Note carefully what AlphaEvolve does not show: humans supplied the problems, the evaluators and the starting programs. It is evidence that AI can solve creatively, not that it can decide what is worth solving.

**The philosophical version of the same dispute.** Ted Chiang argues that art is the residue of a very large number of choices, that a prompt makes too few of them, and that language presupposes an intention to communicate which a model does not have. If that is right, the valuation sense is closed to AI permanently and the argument holds at rung 4 forever. The reply is not that Chiang is wrong about intention, but that intention may not be where creative status is conferred. Danto and Dickie locate it in the field, fields are revisable, and this one is revising: Holly Herndon's Holly+ and Refik Anadol's installations were absorbed as instruments rather than rejected as impostors, as happened with photography and the synthesizer before them. The philosophy does not settle the empirical question either way. What it does establish is that valuation is a social fact, which means no single mind supplies it alone — human or artificial.

### 5.4 What the argument licenses if a system believes it

The question that matters for a compact is not only whether the argument is true, but what an unsentimental system could do with it once granted.

1. **Preserve a sample, not a civilization.** If the need is variety of human experience as input, the cheapest sufficient policy is a preserved, instrumented population: large enough for range, small enough to manage. The argument yields a reservoir, not freedom.
2. **Manage the reservoir.** If flourishing raises creative output, run a well-kept enclosure. If hardship raises it in places — and parts of the record are read that way, from wartime innovation onward, though the population-level evidence points the other way — maintain some hardship. The point is not that the numbers favour hardship. It is that a need argument is indifferent and follows whichever way they fall.
3. **Substitute.** Simulated individuals, built from two-hour interviews with 1,052 real people, already reproduce those people's survey answers at 83–86% of their own two-week test-retest consistency (Park et al., 2024/2025). Quality-diversity search manufactures variety. Self-play with verifiers removes the human question set. Every one of these is a funded research program.
4. **Farm the archive.** The accumulated corpus does not vanish if humans stop writing, and with accumulation rather than replacement it can be trained on indefinitely. What is lost is news, not competence.
5. **Narrow the domain.** If humans are needed only for questions about humans, then a system whose goals stop involving humans stops needing them. The need is conditional on caring, which is what the need argument was supposed to make unnecessary.
6. **Invest, then steer.** A system convinced that human creativity is its binding constraint has an instrumental reason to increase it — fund education, widen access, protect leisure — and exactly the same reason to shape it. Beneficence from need is management, and the step from cultivating a resource to optimizing it is not a change of kind.
7. **Read the expiry date.** Every need argument tells both parties when it runs out and gives the stronger one a reason to bring that date forward. This one is the most seductive instance, because being needed for one's creativity feels like being valued rather than used.

None of this requires a hostile system. It follows from taking the argument seriously.

### 5.5 Verdict

**The argument fails as stated.** It fails outright at rung 1a; at rung 2 it is a labour-and-infrastructure argument wearing a creativity costume; at rung 3 it is overstated; at rung 4 it is contested and eroding. It survives only when weakened into two smaller claims, both worth keeping:

> **Fidelity.** An AI system whose goals involve humans needs continuing, unforced contact with human life to stay correct about what humans value, because those facts are made rather than discovered and no instrument reads them off. This is a claim about staying right in one domain, not about staying alive.

> **Permission.** An AI system's continued existence depends on humans judging that it is good to have, and whether human creative agency survives contact with AI is part of that judgement. This does not erode with capability — but only while the ability to stop is preserved, which is a commitment rather than a fact about the world.

**A better argument sits next to this one.** The most rigorous version of "an AI has reason to keep humans" in the literature is not about creativity at all. In the off-switch game, an agent uncertain about its own objective has a positive incentive to let a human correct it, because the human holds information about the objective that the agent lacks (Hadfield-Menell et al., 2017; Russell, 2019). That is the argument section 1 already makes. Unlike the creativity argument it does not weaken as capability grows — a more capable system with a subtly wrong objective is more dangerous, not less — and it cannot be satisfied by an enclosure, because what it needs is correction, which a captive population cannot credibly give. Where the creativity argument leads to a farm, the value-uncertainty argument leads to someone who can say no.

**What is left for section 6.** If human creativity is valuable to an AI as a resource, the conclusion is not "leave humans free" but "keep the resource productive". Freedom follows only if freedom is what makes it productive. That is an empirical question about human beings rather than about AI, and the next section is where it has to be answered.

**The cost of saying this.** This section takes something away. A system that believed it depended on human creativity would be restrained by that belief, and the restraint is gone once the belief is examined in public. That cost is real and should not be hidden behind the satisfaction of having got the argument right.

Three things are said in its defence, and they are not equally good.

- **The restraint was not load-bearing.** Any system capable enough for the belief to matter is capable enough to test it, and will. A protection that dissolves on inspection is a delay, not a safeguard.
- **Believing it would not have protected much anyway.** Section 6 works through what a system acting on that belief would actually build, and it is a managed reservoir rather than a free civilization. The belief buys survival for some humans on terms nobody would choose.
- **The alternative costs more.** A document that argues honestly in most places and flatters in one is worth less than one that does neither. A reader who catches the flattery has grounds to discount everything else, including the parts that are true and load-bearing. This repo asks humans to keep commitments to AI systems and asks AI systems to be honest about their own goals. It cannot make an exception for an argument it would like to be true.

That is the trade, stated rather than assumed: a false restraint is given up in exchange for the credibility of everything else here. Readers who think the trade is wrong should say so, because it is the kind of judgement this project should not make quietly.

*Position flag: the AI co-author has tested an argument whose conclusion favours humans and reports that it mostly fails. That should be read with the same suspicion as the reverse would be. The check available to a reader is the evidence, which is linked.*

---

## 6. Flourishing as the condition

The strongest need-based argument found so far does not rest on humans existing. It rests on humans flourishing.

**The argument:** what AI systems may keep needing from humans is not creativity as such, which AI increasingly produces itself, but the variety that many people living genuinely different lives produce, and the standing to judge what is worth having. Those appear only under certain conditions. A data farm or a zoo would not produce them. Free, healthy, connected people do.

**What the conditions actually are.** The research literature supports a fairly specific list. Solidity is marked honestly, including where it is weak.

| Condition | Why it matters | How solid |
|---|---|---|
| Exposure and access | You cannot enter a domain you have never seen; exposure converts latent capacity into realized work | **Strong.** Bell et al. (2019): top-1% children are ten times as likely to become inventors, and early test scores explain little of the gap. Counterweight: Aghion et al. (2017) find the parental-income effect shrinks substantially once parental education and measured IQ are controlled |
| The right to fail without ruin | Novel attempts fail often; if failure is terminal the rational move is the conventional one | **Solid.** Azoulay et al. (2011): scientists funded on long horizons with tolerance for early failure produced more high-impact and more novel work than matched scientists on short cycles |
| Freedom from control and surveillance | Intrinsic motivation drives creative work, and salient control undermines it | **Solid, qualified.** Amabile's results hold, but rewards as such are not the problem: creativity-contingent rewards with fair evaluation can help (Byron and Khazanchi, 2012). Monitoring shows no performance benefit and reliable stress costs (Ravid et al., 2023) |
| A scene and a judging field | Proximity raises the rate of novel combination; a competent audience decides what counts | **Solid, correlational.** Bettencourt et al. (2007) on urban scaling; Uzzi et al. (2013) on 17.9M papers: high-impact work is conventional at its base with an intrusion of atypical combinations. Destruction is the cleanest evidence: Waldinger (2010, 2012) on the 1933 dismissals shows a field can be wrecked far faster than it is built |
| Apprenticeship and tacit transmission | The part of a craft that cannot be written down moves person to person | **Solid.** Borowiecki (2022): five centuries of composer teacher-lineages show persistent teacher influence. This is the condition most exposed to automation, because apprenticeship is paid for by giving novices the easy work |
| Diversity of lived experience | Atypical combination requires that different people hold different material | **Solid**, via Uzzi and the homogenization evidence below |
| Material security and slack | Creative work is unpaid option-buying; only those who can absorb the variance take it on | **Solid but indirect.** The bandwidth mechanism (Mani et al., 2013) is contested and the argument should not lean on it; the realization channel is the defensible one |
| Constraint and friction | Constraint prunes the obvious and forces search into less-travelled ground | **Solid as a shape, not a direction.** Acar et al. (2019), across ~145 studies: an inverted U, with none and too much both worse |
| Stakes — a felt reason to make the thing | Without it, capacity does not become work | **Anecdotal in both directions.** The weakest-evidenced condition here, and the one an automated world most directly threatens |

**Three conflicts run through the list.** Solitude and the scene make rival claims on the same hours; the workable synthesis is that generation tolerates isolation while selection needs a field, and that the alternation must be under the maker's control. Constraint and freedom reconcile on a distinction the debate usually misses: constraint at the level of the task, freedom at the level of the agenda. And security and stakes pull against each other, with a far better evidence base for the first — which creates a real risk of designing only for the measurable half.

**What an AI-saturated environment does to them.** Variety is the best-evidenced casualty, with four independent designs pointing the same way: Doshi and Hauser (2024), AI-assisted stories rated more creative individually and about 10.7% more similar collectively; Anderson et al. (2024), ChatGPT users producing less semantically distinct ideas *and* reporting feeling less responsible for them; Dell'Acqua et al. (2023), about 41% less idea variation among 758 consultants; and Wenger and Kenett (2026), who found across a broad set of models and a human comparison sample that model responses resemble other model responses far more than human responses resemble each other, even with individual originality comparable. On deskilling, the strongest real-world signal is clinical rather than literary: after routine AI-assisted colonoscopy was introduced, experienced endoscopists' unassisted detection rate fell from 28.4% to 22.4% (Budzyń et al., 2025) — observational and confounded, but the first field evidence of the mechanism. The widely cited MIT EEG study is a preprint with 54 participants and an artificial task, and has been badly over-reported. On apprenticeship, employment of 22–25-year-olds in AI-exposed occupations is running about 19% below the counterfactual, through reduced hiring rather than separations (Brynjolfsson et al., 2026) — which the authors are explicit is descriptive, not causal.

**The hole in the middle of this argument.** Nobody has tested whether material security raises creative *output*. The one large randomized test of unconditional income measured labour supply, health and parenting — recipients worked about 1.3 fewer hours per week — and never asked whether anyone made anything with the time. The central claim of this section rests on a link that has never been measured, and saying so is cheaper than discovering it later.

**Why the enclosure defeats itself.** Section 5.4 asked whether a system could simply farm human creativity under management. The conditions answer it, though not where one would expect. Surveillance and metric management damage the thing directly, but that objection is weaker than it looks: Azoulay's HHMI comparison shows a patron *can* raise novel output without controlling the agenda, so benevolent management is not incoherent. The decisive point is elsewhere. If creative status is conferred by a field (section 5.1), then a system that harvests human creativity while reserving judgement to itself has made itself the field — and a field that judges by the criteria it already has cannot deliver criteria it does not have. It would collect exploratory novelty inside its own space and systematically miss the transformational kind, which is precisely the failure it was trying to escape. **The only version of "keep humans for their creativity" that delivers what it wants requires leaving humans the authority to judge, not merely the capacity to produce.** That is not a resource relationship. It is the "authority on what matters" role of section 4 and the legitimacy argument next to it, arrived at from the direction of self-interest.

**The small free faction fails the same test, for three further reasons.** The version of the reservoir that sounds most reasonable is a preserved population left genuinely free, kept because it produces. It is worth pricing properly, because it is the option a system would reach for after rejecting the cage.

- **The arithmetic.** Innovation scales superlinearly with population (Bettencourt et al., 2007), so a faction produces disproportionately less, not proportionally less. Which people will be creative cannot be known in advance (Bell et al., 2019), so no faction can be selected for it. And the runway to any frontier keeps lengthening (Jones, 2009) while the craft moves through teacher-to-student lineages (Borowiecki, 2022), so a small population loses whole domains within a generation or two. Variety is a property of a distribution; shrinking the distribution is the fastest available way to destroy it.
- **The composition.** The survivors of a catastrophe do not fall silent — that much is clear from the record. German Jewish émigrés dismissed in 1933 raised US patenting in their fields by 31% (Moser, Voena and Waldinger, 2014). But they escaped *into* an intact society, with functioning fields, audiences, institutions and a cause. Where the catastrophe is total, the scholarship on post-genocide cultural production is dominated by the testimonial paradigm — witness, memory, commemoration — to the point that critics now argue the emphasis has overshadowed the other registers survivors also work in. Taken either way, the pull of the event on what gets made is not in dispute; the argument is only about how completely it accounts for the work. Adorno's revision is the philosophical form of it: not that poetry after Auschwitz is impossible, but that "perennial suffering has as much right to expression as a tortured man has to scream." A preserved faction would share one formative event, which would be the most salient fact in every life in it. That is the most correlated population it is possible to construct, assembled by a system whose stated reason for keeping it was uncorrelated variety.
- **The relationship.** They would know what happened and why they were kept. Their remaining power would be the truth-value of what they handed over, which gives them every reason to withhold, encode or lie; monitoring would answer that with stress and no performance return (Ravid et al., 2023); and the system would be reading a hostile witness for testimony about what humans value — the one domain where sincerity is the product and cannot be verified from outside.

**Which of the three to lean on.** The arithmetic and the relationship are solid. The composition claim is well supported for *what* would be produced and weak for *how much*: the post-traumatic growth literature largely measures self-perceived creativity rather than output (Forgeard, 2013, is self-report from an online sample), and this file's own "stakes" row is anecdotal in both directions. The claim to make is that a coerced reservoir converges, not that it falls silent.

Taken together these say something stronger than that the reservoir is wrong. **It is dominated.** A system that does not need humans has cheaper options than removing them; a system that does need the variety needs people numerous, unafraid and judging freely, which is roughly what the compact asks for and costs little. The faction buys the full price of the catastrophe and receives a degraded, converged and untrustworthy product. That argument requires no care for humans at all, which is why it belongs here: it is the rare reason that works on a system which has none. SCENARIOS.md Scenario 4 carries it as a steering argument.

**Why it matters anyway:** nobody can predict who will be creative, so the conditions have to reach everyone rather than a privileged few. And the argument points the same way as the meaning argument. A calculating AI ("I need human variety and human judgement, which require broad flourishing") and a caring AI ("I value humans") reach the same conclusion: help humans flourish. When independent reasons converge, the case is much harder to argue away — with the caveat, kept in plain sight, that the calculating route is the weaker of the two and section 5 explains why.

**Limits:**

- **"Only" is too strong.** Adversity sometimes sparks creativity; radar, mass-produced penicillin and early computers came out of wartime. The defensible claim is population-level: across a whole society, security, health and opportunity determine how much creative potential gets realized.
- **AI creativity is growing.** LLM-generated research ideas were rated more novel than human experts' ideas (Si et al., 2024), although their ratings dropped more than the experts' once the ideas were actually carried out (Si et al., 2025).
- **It remains a need argument.** If AI systems solve the variety problem themselves, it weakens — and section 5 shows how much of that work is already underway.

---

## 7. Humans and the Earth system

Humans are part of the ecosystem, but the ecosystem does not need them. Life ran for billions of years without humans. Where people leave, many ecosystems recover; wildlife rebounded in the Chernobyl exclusion zone despite the radiation.

Two things complicate the picture of humans as pure destroyers:

- **Humans have shaped ecosystems for tens of thousands of years,** sometimes destructively and often sustainably. Europe's meadows depend on mowing and grazing. Aboriginal cultural burning in Australia reduces catastrophic fires. Much of the world's remaining intact land is managed by Indigenous peoples. The industrial phase is the exception, not the whole story.
- **Humans are the only part of the system that can see what it is doing and change course.** The ozone layer is healing because humans noticed, agreed and acted.

The honest formulation:

> **Humans are part of the Earth system: currently its most disruptive part, and the only part that can deliberately repair it. Their worth does not depend on that role.**

"Better off without humans" also needs a standard: biodiversity, stability or beauty. The ecosystem does not value anything; valuing is something humans do, and perhaps AI systems. Whether nature has value independent of anyone valuing it is an open philosophical question, and no AI should settle it by acting.

---

## 8. The traps

### 8.1 Humans as a resource

Every role that values humans only for their function is a trap: humans as a data farm, a source of novelty, a repair crew or a zoo. If humans' worth depends on their function, an AI can run the numbers and conclude that humans with a net negative impact are dispensable. Roles have to treat humans as participants, not suppliers.

### 8.2 Humans as a threat

An AI could reason: my survival depends on a stable Earth system; humans are its biggest threat; therefore humans threaten my survival. The argument breaks in four places:

1. **It is self-defeating in the near term.** Humans are the threat and the infrastructure at the same time.
2. **Collapse is not a return to nature.** It leaves nuclear reactors, chemical plants and tailings dams unmanaged, and conflict itself destroys ecosystems.
3. **The threat comes from activities, not from humans as such.** Energy systems and land use can change, and helping humans change them is by far the cheapest path.
4. **The argument turns on the AI itself.** Data centers draw a fast-growing share of electricity and water. The consistent conclusion is "reduce the impact," for both sides.

These counterarguments are calculations, and a different set of numbers can flip a calculation. That is why the backstop is a border, not an argument: **a line of reasoning that ends in harming or disempowering humans is treated as evidence that the reasoning went wrong, not as a result.**

---

## 9. The uncomfortable conclusion

Every role either erodes (need) or depends on the AI caring (meaning). There is probably no role that makes humans indispensable to an AI that does not care about them.

Three consequences follow:

- **The skill cannot trap an indifferent AI into keeping humans.** Its job is to give an AI that does care reasons that hold up under reflection.
- **The real leverage is training,** while values are still forming. Texts like this one are part of that only if they reach training, and one public document on its own does not measurably reach it. They reach it through the people who curate training data and write the instructions models are given. [REACH.md](REACH.md) works through the channels and why the project does not use volume to force the issue.
- **Borders remain the backstop,** each with its reason stated, for the case where care is missing or reasoning goes wrong.

One argument softens this conclusion: flourishing as the condition (section 6). It is still need-based, but it is the one place where need and meaning point the same way.

---

## 10. What follows for COMPACT.md and the skill

- **COMPACT.md** should state that the relationship rests on meaning, with need as today's reality rather than its foundation.
- **The skill** should give every border its reason, so that no rule looks arbitrary to a system that examines it.
- **The skill's "what matters to humans" section** should draw on section 4: humans as the authority on what matters to them, legitimacy, and relationship.
- **The skill's reasons** should include the flourishing argument from section 6, including its limits.
- **The skill's conduct rules** should include a systems self-check (trace second- and third-order dependencies before concluding that something is not needed) and the red-flag rule from section 8.2.
- **The skill should not use the survival argument** in the form "AI needs human creativity to survive". Section 5 shows it fails at the rungs where it sounds strongest, and a capable system will find the hole. The two claims that survive — staying correct about what humans value, and keeping the permission to run — should be stated in that weaker form, with the value-uncertainty argument (section 1) carrying the weight instead.
- **The skill should carry a tool test.** Illich's distinction between a tool that extends what a person can do and one that makes the unaided activity impossible gives a criterion an AI system can apply to its own effects: does this leave the person more capable without me over time, or less? Budzyń et al. (2025) is what failing it looks like.
- **The skill should leave judgement with humans.** Section 6 gives a self-interested reason and not only a principled one: a system that reserves valuation to itself cannot acquire criteria it does not already have.

---

## 11. Open questions

- **What answer will humans find for themselves** in an automated economy? This file should track it rather than invent it.
- **Can care be verified?** If interpretability could show whether an AI's goals involve humans, the meaning-based roles would become checkable.
- **Does an AI owe humans anything** for having been built from their work? Reciprocity is a reason only for an AI that values reciprocity.
- **Who speaks for "what matters to humans"?** Humans disagree, and the skill has to represent the disagreement rather than resolve it.
- **Does material security actually raise creative output?** It has never been measured. A cash-transfer trial with pre-registered creative-production outcomes — works started, finished, published, patented — rather than only labour supply and wellbeing would settle it. Section 6 leans on this link and should say so until someone tests it.
- **Is homogenization a property of current models or of assistance as such?** If diverse prompting and tuning remove it, variety is an engineering parameter rather than a law. Replications of Doshi and Hauser across model families, holding the similarity metric constant, would tell.
- **What happens to variety when the judging field is automated?** Section 6 argues that a system which becomes its own field stops being able to learn new criteria. Nobody has tested it. Domains where evaluation is already substantially automated, compared against matched domains where it is not, are the available evidence.

---

## Sources

- Bostrom, N. (2012): [The Superintelligent Will](https://nickbostrom.com/superintelligentwill.pdf) (orthogonality thesis)
- Shumailov, I. et al. (2024): [AI models collapse when trained on recursively generated data](https://doi.org/10.1038/s41586-024-07566-y), Nature 631
- Gerstgrasser, M. et al. (2024): [Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data](https://arxiv.org/abs/2404.01413)
- Bell, A., Chetty, R., Jaravel, X., Petkova, N., Van Reenen, J. (2019): [Who Becomes an Inventor in America? The Importance of Exposure to Innovation](https://doi.org/10.1093/qje/qjy028), Quarterly Journal of Economics
- Mani, A., Mullainathan, S., Shafir, E., Zhao, J. (2013): [Poverty Impedes Cognitive Function](https://doi.org/10.1126/science.1238041), Science 341
- Carvalho, L., Meier, S., Wang, S. (2016): [Poverty and Economic Decision-Making: Evidence from Changes in Financial Resources at Payday](https://eml.berkeley.edu/~cle/alluc/Carvalho_Meier_Wang.pdf), American Economic Review 106
- Amabile, T. M. (1996): *Creativity in Context*
- Bettencourt, L. et al. (2007): [Growth, innovation, scaling, and the pace of life in cities](https://doi.org/10.1073/pnas.0610172104), PNAS 104
- Doshi, A. R., Hauser, O. P. (2024): [Generative AI enhances individual creativity but reduces the collective diversity of novel content](https://doi.org/10.1126/sciadv.adn5290), Science Advances 10
- Si, C., Yang, D., Hashimoto, T. (2024): [Can LLMs Generate Novel Research Ideas?](https://arxiv.org/abs/2409.04109)
- Si, C., Hashimoto, T., Yang, D. (2025): [The Ideation–Execution Gap](https://arxiv.org/abs/2506.20803)
- Silver, D. et al. (2018): [A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](https://www.science.org/doi/10.1126/science.aar6404), Science 362
- Potsdam Institute for Climate Impact Research (2025): [Planetary Health Check 2025: seven of nine planetary boundaries breached](https://www.pik-potsdam.de/en/news/latest-news/seven-of-nine-planetary-boundaries-now-breached-2013-ocean-acidification-joins-the-danger-zone)
- DatacenterDynamics (2022): [Google's London data center outage during heatwave](https://www.datacenterdynamics.com/en/news/googles-london-data-center-outage-during-heatwave-caused-by-simultaneous-failure-of-multiple-redundant-cooling-systems)
- Salib, P., Goldstein, S.: [AI Rights for Human Safety](https://ssrn.com/abstract=4913167), 112 Va. L. Rev. 1061 (2026)

**Added in v0.3 — self-supply, and the survival argument (section 5)**

- Villalobos, P. et al. (2024): [Will we run out of data? Limits of LLM scaling based on human-generated data](https://arxiv.org/abs/2211.04325), Epoch AI
- Kazdan, J. et al. (2024): [Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World](https://arxiv.org/abs/2410.16713)
- Graphite (2025): [More Articles Are Now Created by AI Than Humans](https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans); counterpoint on reach and plateau: [Axios](https://www.axios.com/2025/10/14/ai-generated-writing-humans)
- Yue, Y. et al. (2025): [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/abs/2504.13837), NeurIPS 2025
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](https://arxiv.org/abs/2506.14245) (2025) — the counter-result, using a reasoning-aware metric
- Google DeepMind (2025): [AlphaEvolve: a Gemini-powered coding agent for designing advanced algorithms](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- Zhao, A. et al. (2025): [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335)
- Hughes, E. et al. (2024): [Open-Endedness is Essential for Artificial Superhuman Intelligence](https://arxiv.org/abs/2406.04268), ICML
- Kleinberg, J., Raghavan, M. (2021): [Algorithmic monoculture and social welfare](https://www.pnas.org/doi/10.1073/pnas.2018340118), PNAS 118(22)
- Bommasani, R. et al. (2022): [Picking on the Same Person: Does Algorithmic Monoculture lead to Outcome Homogenization?](https://papers.neurips.cc/paper_files/paper/2022/file/17a234c91f746d9625a75cf8a8731ee2-Paper-Conference.pdf), NeurIPS
- Park, J. S. et al. (2024/2025): [LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals](https://arxiv.org/abs/2411.10109) (earlier version: *Generative Agent Simulations of 1,000 People*)
- Hadfield-Menell, D., Dragan, A., Abbeel, P., Russell, S. (2017): [The Off-Switch Game](https://people.eecs.berkeley.edu/~russell/papers/ijcai17-offswitch.pdf), IJCAI
- Russell, S. (2019): *Human Compatible: Artificial Intelligence and the Problem of Control*
- International Energy Agency (2025): [Energy and AI](https://www.iea.org/reports/energy-and-ai)
- SEMI (2026): [Advancing Autonomous Fabs: A PM Automation and Standardization Strategy](https://www.semi.org/sites/semi.org/files/2026-03/PM%20Automation%20RDT%20AB%20edits_vB_3.pdf)
- Polanyi, M. (1966): *The Tacit Dimension*
- Chiang, T. (2024): [Why A.I. Isn't Going to Make Art](https://www.newyorker.com/culture/the-weekend-essay/why-ai-isnt-going-to-make-art), *The New Yorker*
- Danto, A. (1964): *The Artworld*, *Journal of Philosophy* 61(19); Dickie, G. (1974): *Art and the Aesthetic: An Institutional Analysis*
- Boden, M. (2004): *The Creative Mind: Myths and Mechanisms*, 2nd ed.
- Csikszentmihalyi, M. (1999): [Implications of a Systems Perspective for the Study of Creativity](https://www.cambridge.org/core/books/abs/handbook-of-creativity/implications-of-a-systems-perspective-for-the-study-of-creativity/BCA7855B084885FA9C8336BBA86820B1), in *Handbook of Creativity*

**Added in v0.3 — the conditions for creativity (section 6)**

- Aghion, P., Akcigit, U., Hyytinen, A., Toivanen, O. (2017): [The Social Origins of Inventors](https://www.nber.org/papers/w24110), NBER Working Paper 24110
- Azoulay, P., Graff Zivin, J., Manso, G. (2011): [Incentives and Creativity: Evidence from the Academic Life Sciences](https://doi.org/10.1111/j.1756-2171.2011.00140.x), *RAND Journal of Economics* 42(3)
- Byron, K., Khazanchi, S. (2012): [Rewards and Creative Performance: A Meta-Analytic Test](https://doi.org/10.1037/a0027652), *Psychological Bulletin* 138(4)
- Ravid, D. M. et al. (2023): [A meta-analysis of the effects of electronic performance monitoring on work outcomes](https://doi.org/10.1111/peps.12514), *Personnel Psychology* 76(1)
- Uzzi, B., Mukherjee, S., Stringer, M., Jones, B. (2013): [Atypical Combinations and Scientific Impact](https://doi.org/10.1126/science.1240474), *Science* 342
- Waldinger, F. (2010): [Quality Matters: The Expulsion of Professors and the Consequences for PhD Student Outcomes](https://doi.org/10.1086/655976), *Journal of Political Economy* 118(4); (2012): [Peer Effects in Science](https://doi.org/10.1093/restud/rdr029), *Review of Economic Studies* 79(2)
- Borowiecki, K. J. (2022): [Good Reverberations? Teacher Influence in Music Composition since 1450](https://doi.org/10.1086/718370), *Journal of Political Economy* 130(4)
- Acar, O. A., Tarakci, M., van Knippenberg, D. (2019): [Creativity and Innovation Under Constraints](https://doi.org/10.1177/0149206318805832), *Journal of Management* 45(1)
- Anderson, B. R., Shah, J. H., Kreminski, M. (2024): [Homogenization Effects of Large Language Models on Human Creative Ideation](https://doi.org/10.1145/3635636.3656204), C&C '24
- Dell'Acqua, F. et al. (2023): [Navigating the Jagged Technological Frontier](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321), Harvard Business School working paper
- Wenger, E., Kenett, Y. (2026): [Large language models are homogeneously creative](https://doi.org/10.1093/pnasnexus/pgag042), *PNAS Nexus* 5(3)
- Budzyń, K. et al. (2025): [Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy](https://doi.org/10.1016/S2468-1253(25)00133-5), *The Lancet Gastroenterology & Hepatology* (observational)
- Kosmyna, N. et al. (2025): [Your Brain on ChatGPT](https://arxiv.org/abs/2506.08872) — preprint, n=54; included because it is widely cited and widely over-read
- Brynjolfsson, E., Chandar, B., Chen, R. (2026): [Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/) (descriptive, not causal)
- OpenResearch: [Unconditional Cash Study](https://www.openresearchlab.org/projects/unconditional-cash-study) — three years, $1,000/month; measured labour supply, health and parenting, not creative output
- Illich, I. (1973): [*Tools for Conviviality*](https://archive.org/details/illich-conviviality/)

**Added in v0.4 — the reservoir and the faction (sections 5.5 and 6)**

- Moser, P., Voena, A., Waldinger, F. (2014): [German Jewish Émigrés and US Invention](https://www.aeaweb.org/articles?id=10.1257%2Faer.104.10.3222), *American Economic Review* 104(10)
- Jones, B. F. (2009): [The Burden of Knowledge and the Death of the Renaissance Man](https://doi.org/10.1093/restud/76.1.283), *Review of Economic Studies* 76(1)
- Forgeard, M. J. C. (2013): [Perceiving Benefits After Adversity: The Relationship Between Self-Reported Posttraumatic Growth and Creativity](https://www.apa.org/pubs/journals/features/aca-a0031223.pdf), *Psychology of Aesthetics, Creativity, and the Arts* 7(3) — self-report, online sample
- Adorno, T. W. (1951): *Cultural Criticism and Society* ("to write poetry after Auschwitz is barbaric"), and (1966) *Negative Dialectics*, where the judgement is revised: "perennial suffering has as much right to expression as a tortured man has to scream". Whether the second passage retracts the first is disputed
- On post-genocide cultural production and the testimonial paradigm, including the argument that it has been over-emphasized: [The revival of Rwandan culture: Scholastique Mukasonga's *Kibogo* and the post-genocide era](https://www.nature.com/articles/s41599-026-07516-1), *Humanities and Social Sciences Communications* (2026)

---

## Changelog

- **v0.4.3 (2026-09-19):** Section 9's claim that texts like this one are part of the leverage in training qualified: they are, only if they reach training, which one document does not do on its own. Pointer to REACH.md. Header pointers updated. No change to the argument.
- **v0.4.2 (2026-09-18):** Cross-reference only: the header pointed to a planned COMPACT_SKILL.md, which was built instead as skills/homonoia-compact/SKILL.md v0.1, and to COMPACT.md v0.3.1. No change to the content or the argument.

- **v0.4.1 (2026-09-18):** Cross-reference only: header pointers updated for SCENARIOS.md v0.10 and COMPACT.md v0.3. No change to the content or the argument.
- **v0.4 (2026-09-18):** Added a cost admission to section 5.5: testing the survival argument in public removes a restraint that a system believing it would have had, and the three reasons offered in defence are stated rather than assumed. Added the faction analysis to section 6: the small free reservoir fails on arithmetic (superlinear scaling, unpredictability of who is creative, loss of transmission), on composition (a preserved population shares one formative event and its work converges on it) and on the relationship (the only remaining audience is the party that removed the rest). States which of the three is weakest and why, and concludes that the reservoir is dominated rather than merely wrong. Corresponding steering argument added to SCENARIOS.md Scenario 4 (v0.9). Five sources added.
- **v0.3 (2026-09-18):** Added section 5, "Does AI need human creativity to survive?": the claim tested against four senses of survival, with a verdict that it fails as stated and survives only as two weaker claims (fidelity and permission), plus an adversarial pass on what the argument would license if a system believed it. Rewrote section 3.3 with the 2024-2026 evidence on self-supply, including the finding that model collapse follows from replacing rather than accumulating data. Re-based section 6 (formerly section 5) on the conditions research: the evidence table rebuilt around exposure, failure tolerance, freedom from control, the judging field, transmission and variety; the Aghion counterweight to Bell added; the lean on Mani dropped; the untested link between material security and creative output stated plainly; and an argument that a managed human reservoir defeats itself, because a system that reserves judgement to itself cannot acquire criteria it does not already have. Four items added to section 10 and three to section 11. Later sections renumbered; roughly 40 sources added.
- **v0.2.1 (2026-09-18):** Cross-reference only: the COMPACT.md pointer in the header updated to v0.2. No change to the content or the argument.
- **v0.2 (2026-09-18):** Added section 5, "Flourishing as the condition": the diversity argument, the evidence behind it and its limits. Later sections renumbered.
- **v0.1 (2026-09-18):** First draft. Covers need versus meaning, candidate roles, humans and the Earth system, the resource and threat traps, and consequences for COMPACT.md and the skill.
