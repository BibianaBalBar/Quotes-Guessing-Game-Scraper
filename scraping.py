import requests
from bs4 import BeautifulSoup

all_quotes = []

URL = 'http://quotes.toscrape.com/'
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
quotes = soup.find_all(class_="quote")
for quote in quotes:
    all_quotes.append({
        "text":quote.find(class_="text").get_text(),
        "author":quote.find(class_="author").get_text(),
        "bio-link":quote.find("a")["href"]
    })
    
next_btn = soup.find(class_="next")
print(next_btn.find("a")["href"])

# print(all_quotes)