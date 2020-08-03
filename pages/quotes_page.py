from bs4 import BeautifulSoup

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser

from typing import List

class QuotesPage:
    """A class that retreives a web page from a URL, and parses it for quotes"""

    def __init__(self, page: str):
        """
        Parameters
        ----------
        page : str
            The url of the web page.
        """
        self.soup = BeautifulSoup(page, "html.parser")
    
    @property
    def quotes(self) -> List[QuoteParser]:
        """Returns the web page's quotes.
        
        Returns
        -------
        list
            A list of QuoteParser representing the web page's quotes.
        """
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]
    
