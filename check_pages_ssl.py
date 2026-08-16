import urllib.request
import urllib.error
import json
import re

import os

# Leggi il token dalle variabili di ambiente
token = (
    os.environ.get('GH_TOKEN') or
    os.environ.get('GITHUB_TOKEN') or
    os.environ.get('GITHUB_PAT') or
    ''
)

if not token:
    print('ERROR: No GitHub token found in environment')
    exit(1)

print(f"Token prefix: {token[:8]}...")

REPO = "fslmultiservice22/fsl-agentpay-platform"
HEADERS = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'Python/3.11',
}

def api_get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read()), r.status
    except urllib.error.HTTPError as e:
        return json.loads(e.read()), e.code

def api_put(url, data):
    body = json.dumps(data).encode()
    req = urllib.request.Request(url, data=body, headers={**HEADERS, 'Content-Type': 'application/json'}, method='PUT')
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read()) if r.length else {}, r.status
    except urllib.error.HTTPError as e:
        return json.loads(e.read()), e.code

# 1. Verifica stato attuale GitHub Pages
print("\n=== GitHub Pages Status ===")
data, status = api_get(f"https://api.github.com/repos/{REPO}/pages")
print(f"HTTP Status: {status}")
if status == 200:
    print(f"Pages status: {data.get('status')}")
    print(f"Custom domain: {data.get('custom_domain')}")
    print(f"HTTPS enforced: {data.get('https_enforced')}")
    cert = data.get('https_certificate', {})
    print(f"HTTPS cert state: {cert.get('state')}")
    print(f"HTTPS cert errors: {cert.get('errors')}")
    print(f"HTTPS cert domains: {cert.get('domains')}")
else:
    print(f"Error: {data}")

# 2. Prova ad abilitare HTTPS enforce
print("\n=== Enabling HTTPS Enforce ===")
result, status = api_put(
    f"https://api.github.com/repos/{REPO}/pages",
    {"https_enforced": True}
)
print(f"HTTP Status: {status}")
if status in (200, 204):
    print("HTTPS enforce enabled successfully!")
else:
    print(f"Result: {result}")

# 3. Verifica stato dopo
print("\n=== GitHub Pages Status After ===")
data, status = api_get(f"https://api.github.com/repos/{REPO}/pages")
if status == 200:
    cert = data.get('https_certificate', {})
    print(f"HTTPS enforced: {data.get('https_enforced')}")
    print(f"HTTPS cert state: {cert.get('state')}")
    print(f"HTTPS cert errors: {cert.get('errors')}")
