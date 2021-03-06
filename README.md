<p align="center"><img src="./images/logos/web-scraping.jpg" alt="Web scraping logo." ><p>

# Quote Scraper

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Screenshots](#screenshots)
- [Launch](#launch)
- [Technologies](#technologies)

## Introduction
Quote scraper is a simple python application that scrapes the web page at http://quotes.toscrape.com.

The purpose of this application was to become more familiar with web scraping.

## Features
- Scrapes the web page http://quotes.toscrape.com

## Screenshots
<img src="./images/screenshots/main.PNG" alt="A screenshot of the application being run in the console. It shows the div tags of class quote of a web page.">

## Launch
To run, in the console enter:
```
python app.py
```

## Technologies
- [Python 3.8.3](https://www.python.org/downloads/release/python-383/)
### Python Modules
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
    - Allows a web page to be scraped (parses its HTML or XML)
- [requests](https://pypi.org/project/requests/)
    - Allows sending HTTP requests
