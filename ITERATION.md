cat > ~/hw8-toolkit/ITERATION.md <<'EOF'
# Iteration

## What went wrong
It skipped over important details. You couldn't tell if the skill had even loaded.

![v1 run on Fridge Roulette](evidence/run1-v1.png)

## Why
Not specific enough instructions. Nothing required evidence; it was only in the format line.

## What I changed
I added a rule: every line needs a command and its result, or it's SKIPPED. Compare `evidence/SKILL-v1.md` with `skills/api-key-check/SKILL.md`.

## Rerun
Yes, it worked, as additional checks were added.

![v2 catching a planted fake key](evidence/run2-v2-leak.png)
![v2 on this repo before pushing](evidence/run3-toolkit.png)
EOF