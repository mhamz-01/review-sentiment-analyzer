# If testing locally:  BASE_URL = "http://localhost:8000"
# If testing via ngrok: BASE_URL = "https://xxxx.ngrok.io"

import requests
import json

# ---- CHANGE THIS TO YOUR NGROK URL IF TESTING REMOTELY ----
BASE_URL = "https://carefully-stegosaur-ranting.ngrok-free.dev/"


def pretty_print(title, response):
    """Print the response in a readable format."""
    print(f"\n{'=' * 55}")
    print(f"  {title}")
    print(f"{'=' * 55}")
    print(json.dumps(response.json(), indent=2))


# ============================================================
# TEST 1: /analyze endpoint with 3 sample reviews
# ============================================================
print("\n>>> TEST 1: Single Review Analysis (/analyze)")

test_reviews = [
    "This product is amazing, I love it",
    "Complete waste of money, very disappointed",
    "It works but could be better",
]

for review in test_reviews:
    response = requests.post(
        f"{BASE_URL}/analyze",
        json={"review_text": review}
    )
    pretty_print(f'Review: "{review}"', response)


# ============================================================
# TEST 2: /analyze_from_url endpoint with Amazon product URL
# ============================================================
print("\n>>> TEST 2: Analyze Reviews from Amazon URL (/analyze_from_url)")


# For testing this link should be safely accessed as sometimes amazon server detects the automated script and block it
amazon_url = "https://www.amazon.com/dp/B09N4D5VHV"

response = requests.post(
    f"{BASE_URL}/analyze_from_url",
    params={"url": amazon_url, "num_reviews": 15}
)

pretty_print("Amazon URL Analysis Result", response)