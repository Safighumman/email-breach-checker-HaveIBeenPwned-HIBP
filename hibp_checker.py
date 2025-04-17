
---

## 🐍 `hibp_checker.py`

```python
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("HIBP_API_KEY")
BASE_URL = "https://haveibeenpwned.com/api/v3/breachedaccount/"

HEADERS = {
    "hibp-api-key": API_KEY,
    "user-agent": "email-breach-checker"
}

def check_email(email):
    url = f"{BASE_URL}{email}?truncateResponse=false"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        breaches = response.json()
        print(f"\n[!] Email found in {len(breaches)} breach(es):\n")
        for idx, breach in enumerate(breaches, 1):
            print(f"{idx}. Breach: {breach['Name']} ({breach['BreachDate']})")
            print(f"   - Data: {', '.join(breach['DataClasses'])}")
            print(f"   - Verified: {breach['IsVerified']}")
            print("")
    elif response.status_code == 404:
        print(f"\n[✓] {email} was NOT found in any known breach.")
    else:
        print(f"[!] API error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print("=== Email Breach Checker ===")
    user_email = input("Enter email address: ").strip()
    check_email(user_email)
