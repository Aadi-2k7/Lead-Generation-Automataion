import requests
from bs4 import BeautifulSoup
from config import HEADERS

def scrape_companies():
    url = "https://www.yellowpages.com/search?search_terms=software+companies&geo_location_terms=India"
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        data = []
        listings = soup.select(".result")

        for item in listings[:30]:
            name = item.select_one(".business-name")
            location = item.select_one(".locality")
            website = item.select_one(".track-visit-website")

            data.append({
                "name": name.text.strip() if name else None,
                "location": location.text.strip() if location else None,
                "website": website["href"] if website else None
            })

        return data

    except Exception as e:
        print("Scraping failed:", e)
        return []