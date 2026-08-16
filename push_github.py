#!/usr/bin/env python3
"""Push index.html to GitHub via API using token from environment."""
import base64, json, urllib.request, os, sys

REPO = "fslmultiservice22/fsl-agentpay-platform"
FILE = "index.html"

# Try multiple token sources
TOKEN = (
    os.environ.get("GITHUB_PAT") or
    os.environ.get("GH_TOKEN") or
    os.environ.get("GITHUB_TOKEN") or
    ""
)

if not TOKEN:
    print("ERROR: No GitHub token found in GITHUB_PAT, GH_TOKEN, or GITHUB_TOKEN env vars")
    sys.exit(1)

print(f"Using token: {TOKEN[:8]}...")

# Read updated file
with open(FILE, "rb") as f:
    content = base64.b64encode(f.read()).decode()

# Get current SHA
req = urllib.request.Request(
    f"https://api.github.com/repos/{REPO}/contents/{FILE}",
    headers={
        "User-Agent": "AgentPay-Bot",
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}",
    }
)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
sha = data["sha"]
print(f"Current SHA: {sha[:10]}")

# Push update
payload = json.dumps({
    "message": "v61+v62: sezione Blog/Aggiornamenti, link navbar, CurrencyWidget, TipCalculatorWidget",
    "content": content,
    "sha": sha,
    "branch": "main",
}).encode()

req2 = urllib.request.Request(
    f"https://api.github.com/repos/{REPO}/contents/{FILE}",
    data=payload,
    method="PUT",
    headers={
        "User-Agent": "AgentPay-Bot",
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}",
        "Content-Type": "application/json",
    }
)
with urllib.request.urlopen(req2) as r:
    result = json.loads(r.read())
print(f"SUCCESS! New SHA: {result['content']['sha'][:10]}")
print(f"Commit: {result['commit']['sha'][:10]}")
print(f"Message: {result['commit']['message']}")
