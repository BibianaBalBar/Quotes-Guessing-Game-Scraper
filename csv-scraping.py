import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter



URL_base = 'http://quotes.toscrape.com'


def scrape_quotes():
    all_quotes = []
    url = '/page/1'
    while url:
        page = requests.get(f"{URL_base}{url}")    
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
        sleep(1)
    return all_quotes


# pass quotes to csv file
def write_quotes(quotes):
    with open("quotes.csv", "w", encoding="utf-8") as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)