import requests

from pages.quotes_page import QuotesPage

# if in script form
if __name__ == "__main__":
    URL = "http://quotes.toscrape.com"
    page_content = requests.get(URL).content
    page = QuotesPage(page_content)
    print(f"Quotes of the webpage at the url: {URL}\n")
    for quote in page.quotes:
        print(quote)