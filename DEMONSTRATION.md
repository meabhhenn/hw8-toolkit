cat > ~/hw8-toolkit/DEMONSTRATION.md <<'EOF'
# Demonstration

## Task
Testing with a fake planted key. I also ran it on my real repos before pushing (Fridge Roulette and this toolkit) and used the MCP tool to find real recipes.

## MCP tool call
![find_recipes call in Codex](evidence/mcp-tool-call.png)

## Runs
![Run 1, v1 on Fridge Roulette](evidence/run1-v1.png)
![Run 2, v2 with a fake planted key](evidence/run2-v2-leak.png)
![Run 3, v2 on hw8-toolkit](evidence/run3-toolkit.png)

## Did I agree with the checker?
**RISK vs LEAK:** Neutral. I think it's a word that can mean different things to different people, and to me RISK is better because it was describing risks to the safety and privacy of the app user.

**Reading my real .env:** No. I think there should have been an additional request to see if that was appropriate before that action was executed, but more importantly, it should not be necessary unless anyone can access .env.

**Skipping browser exposure:** No, it didn't annoy me. It's better to admit it couldn't check than to falsely say OK.
EOF