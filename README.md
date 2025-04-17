# 🛡️ Email Breach Checker (HaveIBeenPwned API)

This tool checks if an email address or domain has been involved in a known data breach using the HaveIBeenPwned API.

Perfect for learning about personal data exposure, privacy hygiene, and how public breach data can be queried safely.

---

## 🔍 Features

- Checks email addresses against public data breaches
- Uses official HaveIBeenPwned API (v3)
- Optional domain search
- Highlights each breach with details like breach date, exposed data, and verified status

---

## ⚙️ Setup

1. Clone the repo:

        ```bash
    git clone https://github.com/yourusername/email-breach-checker.git
    cd email-breach-checker)

2. Install requirements:

    pip install -r requirements.txt


3. Add your HIBP API key to a .env file:

    HIBP_API_KEY=your_key_here


---

## 🚀 Usage
    Run the script:
        python3 hibp_checker.py



  Follow the prompts to enter an email or domain.
---

## 📸 Example Output

=== Email Breach Checker ===
Enter email address: johndoe@example.com

[!] Email found in 3 breaches:

1. Breach: LinkedIn (2016)
   - Data: Emails, Passwords
   - Verified: True

2. Breach: Adobe (2013)
   - Data: Emails, Password hints
   - Verified: True

3. Breach: RandomForum
   - Data: Emails, IPs
   - Verified: False


---

## 🛑 Disclaimer
This tool is for educational and personal security awareness only. Do not use it to check emails without consent.
---
## 🧠 Educational Value
-API authentication

-Working with JSON responses

-Understanding data exposure risks
---

## ⭐ Show Support
If this helps you or someone else, consider giving it a ⭐!
