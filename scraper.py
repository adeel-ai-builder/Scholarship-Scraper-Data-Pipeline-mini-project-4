import requests
from bs4 import BeautifulSoup
from parser import parse_scholarships

base_url = "https://quotes.toscrape.com/page/{}/"
HEADERS={
    "User-Agent": "Mozilla/5.0"
}

def scrape_all_pages(total_pages=5):
    all_scholarship=[]

    for page in range(1, total_pages + 1):
        print(f"Scraping Page : {page}.....")
        url=base_url.format(page)

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            soup=BeautifulSoup(response.text, "html.parser")
            page_data=parse_scholarships(soup)
            all_scholarship.extend(page_data)

        except requests.exceptions.RequestException as e:
            print(f"Error on Page {page} : {e}..")
    
    return all_scholarship