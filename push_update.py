import base64, json, urllib.request, os, sys

REPO = "fslmultiservice22/fsl-agentpay-platform"
FILE = "index.html"
TOKEN = os.environ.get("GITHUB_PAT", "")

if not TOKEN:
    # Prova a leggere da git credential
    import subprocess
    result = subprocess.run(
        ["git", "config", "--global", "credential.helper"],
        capture_output=True, text=True
    )
    print("Credential helper:", result.stdout.strip())
    # Prova con SSH agent o altro
    print("No GITHUB_PAT set. Please set GITHUB_PAT env var.")
    sys.exit(1)

# Leggi il file aggiornato
with open(FILE, "rb") as f:
    content = base64.b64encode(f.read()).decode()

# Ottieni SHA del file attuale
req = urllib.request.Request(
    f"https://api.github.com/repos/{REPO}/contents/{FILE}",
    headers={
        "User-Agent": "AgentPay",
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}",
    }
)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
sha = data["sha"]
print("Current SHA:", sha[:10])

# Aggiorna il file
payload = json.dumps({
    "message": "v61: sezione Blog/Aggiornamenti (3 articoli), link navbar; CurrencyWidget app",
    "content": content,
    "sha": sha,
    "branch": "main",
}).encode()

req2 = urllib.request.Request(
    f"https://api.github.com/repos/{REPO}/contents/{FILE}",
    data=payload,
    method="PUT",
    headers={
        "User-Agent": "AgentPay",
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}",
        "Content-Type": "application/json",
    }
)
with urllib.request.urlopen(req2) as r:
    result = json.loads(r.read())
print("Updated! New SHA:", result["content"]["sha"][:10])
print("Commit:", result["commit"]["sha"][:10])
