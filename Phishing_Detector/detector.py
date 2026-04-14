import re
import config

def scan_email(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read().lower()

        # Logic: Find words from our config list
        found = [word for word in config.SUSPICIOUS_KEYWORDS if word in content]
        
        # Logic: Look for links
        has_link = "http" in content
        
        score = len(found)
        if has_link: score += 2

        print(f"\n--- Scanning {file_name} ---")
        if score >= config.RISK_THRESHOLD:
            print(f"STATUS: [!] HIGH RISK (Score: {score})")
            print(f"Found: {found}")
        else:
            print(f"STATUS: [✓] LOW RISK (Score: {score})")

    except Exception as e:
        print(f"Error: {e}")

scan_email('emails.txt')