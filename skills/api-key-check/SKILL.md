---
name: api-key-check
description: Checks a repo for leaked API keys and secrets before committing, pushing, deploying, or submitting. Reports problems only and never edits files. Use whenever a project uses an API key, a .env file, or a third-party API, or the user asks if something is safe to push.
---

# API Key Check (v2)

## What to do
1. List what git tracks and ignores: `git ls-files` and `git status --ignored`.
2. Check that every .env file is actually ignored: `git check-ignore -v <path>` for each .env found (including in subfolders).
3. Search tracked files for key-like values: strings starting with `sk-` or `AIza`, and anything assigned to a variable named like KEY, TOKEN, or SECRET.
4. Search git history for keys that were committed and later deleted: `git log --all -p`.
5. Check whether any key reaches the browser: keys in .html files, frontend .js files, or env vars with VITE_ or NEXT_PUBLIC_ prefixes.
6. Check that `.env.example` exists and contains only placeholders.

## Output format
First line: `api-key-check v2 report`
Then one line per check:
`[OK | LEAK | RISK | SKIPPED] <check> — <command run> → <what it returned, or file:line>`
Final line: `Verdict: SAFE TO PUSH` or `Verdict: DO NOT PUSH — <most urgent fix>`

## Rules
- Every line needs evidence: the exact command you ran and its result, or a file and line. A check with no evidence is SKIPPED, not OK.
- Never create, edit, or delete files. Never run git commands that change anything (no add, commit, rm, reset).
- Never print a full secret. Show the first 4 characters, then `…`.
- A key that was ever committed counts as a LEAK even if it's deleted now. Say to revoke it.
