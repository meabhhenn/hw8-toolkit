import json, os, sys, urllib.parse, urllib.request
from pathlib import Path
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv(Path(__file__).parent / ".env")
mcp = FastMCP("recipes")

@mcp.tool()
def find_recipes(ingredients: str, number: int = 5) -> str:
    """Find real recipes that use ingredients the user already has, from the Spoonacular API.

    Use this whenever the user asks what they can cook with specific ingredients,
    or needs real recipe data instead of invented recipes.
    ingredients: comma-separated, e.g. "eggs, rice, spinach". number: 1-10 recipes.
    Returns one line per recipe: title, ingredients used, ingredients missing, link.
    """
    key = os.environ.get("SPOONACULAR_API_KEY")
    if not key:
        return "Error: SPOONACULAR_API_KEY is not set. Put it in mcp-server/.env."
    number = max(1, min(int(number), 10))
    query = urllib.parse.urlencode({"ingredients": ingredients, "number": number,
                                    "ranking": 1, "ignorePantry": "true", "apiKey": key})
    try:
        with urllib.request.urlopen(
                "https://api.spoonacular.com/recipes/findByIngredients?" + query,
                timeout=15) as resp:
            recipes = json.load(resp)
    except Exception as e:
        # log to stderr only: stdout is the MCP protocol channel
        print(f"Spoonacular request failed: {type(e).__name__}", file=sys.stderr)
        return f"Error: Spoonacular request failed ({type(e).__name__}). Check the key or daily quota."
    if not recipes:
        return f"No recipes found for: {ingredients}"
    lines = []
    for r in recipes:
        used = ", ".join(i["name"] for i in r.get("usedIngredients", []))
        missing = ", ".join(i["name"] for i in r.get("missedIngredients", [])) or "nothing"
        slug = r["title"].lower().replace(" ", "-")
        lines.append(f"{r['title']} | uses: {used} | missing: {missing} | "
                     f"https://spoonacular.com/recipes/{slug}-{r['id']}")
    return "\n".join(lines)

if __name__ == "__main__":
    mcp.run()
