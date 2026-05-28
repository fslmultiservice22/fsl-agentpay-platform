#!/usr/bin/env python3
"""Update README.md on GitHub to fix the live URL."""
import base64, json, urllib.request, os

REPO = "fslmultiservice22/fsl-agentpay-platform"
FILE = "README.md"
TOKEN = os.environ.get("GH_TOKEN", "")

headers = {
    "User-Agent": "AgentPay-Bot",
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {TOKEN}",
}

# Get current README
req = urllib.request.Request(
    f"https://api.github.com/repos/{REPO}/contents/{FILE}",
    headers=headers
)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())

sha = data["sha"]
current_content = base64.b64decode(data["content"]).decode("utf-8")
print("Current README (first 200 chars):", current_content[:200])

# Fix the URL
new_content = current_content.replace(
    "🌐 Live: app.fslditta.com",
    "🌐 Live: agentpay.fslditta.com"
).replace(
    "app.fslditta.com",
    "agentpay.fslditta.com"
)

if new_content == current_content:
    print("No changes needed — URL already correct or not found")
else:
    # Push update
    payload = json.dumps({
        "message": "fix: correggi URL live da app.fslditta.com a agentpay.fslditta.com",
        "content": base64.b64encode(new_content.encode()).decode(),
        "sha": sha,
        "branch": "main",
    }).encode()

    req2 = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/contents/{FILE}",
        data=payload,
        method="PUT",
        headers={**headers, "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req2) as r:
        result = json.loads(r.read())
    print(f"README updated! Commit: {result['commit']['sha'][:10]}")
