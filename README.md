cat > ~/hw8-toolkit/README.md <<'EOF'
# HW8 Toolkit: api-key-check + recipes MCP

## What's here
- **api-key-check (skill):** Checks a repo for leaked API keys before you push, and only reports. It tells you whether it's safe to push, with proof for each check. It triggers when I ask "is this safe to push?"
- **recipes (MCP server):** A `find_recipes` tool that gives back real recipes from Spoonacular for the ingredients you have, with each recipe's ingredients used, ingredients missing, and a link.

## Why I built it
**The skill:** In HW6 I pasted my API key into `.gitignore`. I had a misunderstanding of which one gets pushed or not. I was scared, I feel that I should be way more careful, and I was surprised that AI didn't catch that for me.

**The MCP tool:** I picked Spoonacular because it was easy to test and I already had a working key from Project 2. I also wanted to improve it because I think it is a really meaningful and good project.

## Install
### Skill
```bash
mkdir -p ~/.codex/skills/api-key-check
cp skills/api-key-check/SKILL.md ~/.codex/skills/api-key-check/
```
Quit and reopen Codex.

### MCP server
```bash
python3 -m venv .venv
.venv/bin/pip install -r mcp-server/requirements.txt
cp mcp-server/.env.example mcp-server/.env   # paste your own Spoonacular key here
```
Get a free key at spoonacular.com/food-api/console. Add this to `~/.codex/config.toml`, then quit and reopen Codex:
```toml
[mcp_servers.recipes]
command = "/Users/meabhhennessy/hw8-toolkit/.venv/bin/python"
args = ["/Users/meabhhennessy/hw8-toolkit/mcp-server/server.py"]
```
⚠️ The `/Users/meabhhennessy/` paths are machine-specific. Replace them with your own.

## Tested in
Codex desktop app (macOS), GPT-6.1 Sol Light.

## Borrowed / adapted
The output format and evidence rule from the course's spec-check example, and the server structure from the MCP Python quickstart.

## How I used AI
Claude drafted the first versions of SKILL.md and server.py. I used it for debugging the mcp 2.x error: the server used `FastMCP`, which was renamed in mcp 2.x, so I pinned `mcp[cli]<2`. I chose the API-key problem from my own HW6 mistake.
EOF