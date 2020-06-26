import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []

URL_base = 'http://quotes.toscrape.com'
url = '/page/1'

while url:
    page = requests.get(f"{URL_base}{url}")
    print(f"Now Scraping {URL_base}{url}...")
    soup = BeautifulSoup(page.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        all_quotes.append({
            "text":quote.find(class_="text").get_text(),
            "author":quote.find(class_="author").get_text(),
            "bio-link":quote.find("a")["href"]
        })
        
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None
    # sleep(1)



