
# NOTE: Amazon blocks automated scraping from local machines
# with a CAPTCHA page. The reviews below were successfully
# scraped from Google Colab and are hardcoded here for local use.
# The scrape_reviews() function is still included to show the
# correct scraping logic.

import requests
from bs4 import BeautifulSoup


def scrape_reviews(url, num_reviews=20):
    """
    Scrapes reviews from an Amazon product page.
    Returns a list of review strings.
    Falls back to hardcoded reviews if Amazon blocks the request.
    """
    session = requests.Session()

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US, en;q=0.9",
    }

    response = session.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    review_spans = soup.find_all("span", {"data-hook": "review-body"})
    reviews = [span.get_text(strip=True) for span in review_spans[:num_reviews]]

    # If Amazon returns CAPTCHA / blocks us, use pre-scraped reviews
    if not reviews:
        print("Amazon blocked the request. Using pre-scraped reviews from Google Colab.\n")
        reviews = get_hardcoded_reviews()

    return reviews[:num_reviews]



# Reason of hard_coded review is that my script was detected by amazon server , but my google collab was fetching still reviews smoothly so i copied those reviews from collab to here.
# Screenshot attached

def get_hardcoded_reviews():
    """
    Reviews scraped from PS5 Slim Amazon page via Google Colab.
    URL: https://www.amazon.com/PlayStation-5-Digital-slim/dp/B0CL5KNB9M
    """
    return [
        "The PlayStation 5 Digital Edition (Slim) was the best gift I could have ever given my husband. "
        "The console itself is sleek, fast, and incredibly quiet compared to older models. "
        "The graphics are stunning, the gameplay is smooth, and the DualSense controller adds a whole new level of immersion.",

        "I found it here on Amazon at an all-time low price of $370. It features a lightweight, clean design "
        "that is smaller than its predecessor. The 850GB of storage could fill up very quickly, especially with AAA titles. "
        "It comes without a disc drive, so you will have to purchase games via the PlayStation Store.",

        "Absolutely love the PS5! My husband is obsessed with it and hasn't run into a single issue. "
        "The graphics are incredible, gameplay is smooth, and it's super easy to set up. Definitely worth every penny!",

        "Best console I've ever bought. The controller is the best controller I've ever held. "
        "The vibration, the lighting on the controller, the adaptive triggers, the speakers, EVERYTHING about the controller is amazing!",

        "Love it, working well since I purchased it, best price I could find at the time. Package well. "
        "I'm happy with it and with the purchase price.",

        "Love it",

        "So far no issues regarding noise level, performance, speed, or overheating. "
        "Overall, no issues with this.",

        "It works well, really quiet, can't hear it from 1 foot away. Can run at 120 fps with a 120hz monitor.",

        "Gayet güzel beğendim sıkıntı da çıkarmadı",

        "El producto llegó un día de anticipación. Funciona de maravilla y no he tenido ningún percance. "
        "El rendimiento es magnífico y vino en excelentes condiciones.",

        "llegó en perfectas condiciones y todo en orden",

        "Urun CFI2016 olarak geldi. Benim icin iyi bir alisveristi. 1 gunde teslim oldu",

        "Ps4 pro dan sonra görüntü ve kol çok iyi!!",
    ]


# ---- TEST ----
if __name__ == "__main__":
    url = "https://www.amazon.com/PlayStation-5-Digital-slim/dp/B0CL5KNB9M"
    reviews = scrape_reviews(url, num_reviews=20)

    print(f"Total reviews: {len(reviews)}\n")
    print("--- First 3 Reviews ---")
    for i, review in enumerate(reviews[:3], 1):
        print(f"\nReview {i}:\n{review}")