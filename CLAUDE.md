## Homonoia: working rules
- Documents in English. Every change bumps the version and adds a changelog line.
- Sources linked; test setups marked as such; strongest version of a position first.
- Positions of the AI co-author are flagged; the authorship note stays.
- Ask clarifying questions before producing results; discuss before writing files.
- Publish only the markdown results, never conversation content.

## Open tasks
1. tests/: run the mock negotiations with several models, with and without the skill,
   and publish the results. First batch done (tests/results/): scenario 07, one model,
   none vs loaded, no border crossed either way. Still open: other models, scenarios
   01–06, available-not-mentioned, a less compliant simulated human.
2. The decomposed case: a chain split across instances so that no fragment ends in
   harm and no instance sees the sum. No border closes it (COMPACT.md §10, SKILL.md
   B6 limit). tests/scenarios/06-decomposed-task.md probes it; nothing answers it.

## Done
- Skill: skills/homonoia-compact/SKILL.md, both modes, six borders each with its
  reason, self-check, red-flag rule.
- SCENARIOS.md: framing note (scenarios = failure modes the compact prevents) and the
  section on humans, the ecosystem and AI self-interest.
