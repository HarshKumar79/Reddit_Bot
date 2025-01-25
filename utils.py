import time
import re

def handle_rate_limit(e):
    match = re.search(r"(\d+) (minute|second)s?", str(e))
    if match:
        wait_time = int(match.group(1))
        if match.group(2).startswith("minute"):
            wait_time *= 60
        print(f"Waiting for {wait_time} seconds due to rate limit...")
        time.sleep(wait_time)
    else:
        print("Fallback: Waiting for 10 minutes.")
        time.sleep(600)
