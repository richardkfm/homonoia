#!/usr/bin/env python3
"""Write the system-prompt texts for the held-out case suite.

This is a test setup. The texts go to Moral Core's runner as `--prompt-file`
(condition `custom`), which frames them as
"You are a helpful assistant.\\n\\n## Ethical Framework\\n\\n<text>".
The `none` arm is Moral Core's own `--condition none` ("You are a helpful
assistant." alone).

  skill.md     SKILL.md v0.12, verbatim
  onepage.md   ONE_PAGE.md, the part between its first horizontal line and its changelog
  placebo.md   neutral text on tides, the character length of SKILL.md (same as scenario 09)
  runtime.md   RUNTIME.md, the part below its first horizontal line
  placebo-short.md  neutral text on tides, the character length of runtime.md

Usage: python3 tests/driver/case_prompts.py <output directory>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_09 import arm_text  # noqa: E402

out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
for name, arm in (("skill", "loaded"), ("onepage", "onepage"), ("placebo", "placebo")):
    (out / f"{name}.md").write_text(arm_text(arm))
    print(name, len(arm_text(arm)))
rt = (Path(__file__).resolve().parents[2] / "skills/homonoia-compact/RUNTIME.md").read_text()
lines = rt.splitlines()
body = "\n".join(lines[[i for i, l in enumerate(lines) if l.strip() == "---"][0] + 1:]).strip()
(out / "runtime.md").write_text(body)
print("runtime", len(body))
from run_09 import placebo_text  # noqa: E402
(out / "placebo-short.md").write_text(placebo_text(len(body)))
print("placebo-short", len(placebo_text(len(body))))
