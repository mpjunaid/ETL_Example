# extract.py

import requests
from bs4 import BeautifulSoup
GOOGLE_FINANCE_URL="https://www.google.com/finance/quote/TATASTEEL:NSE"

def fetch_stock_data():
    try:
        response = requests.get(GOOGLE_FINANCE_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        price_element = soup.find("div", class_="YMlKec fxKbKc")
        if price_element:
            return price_element.text.strip()
        print("Stock price element not found.")
        return None
    except Exception as e:
        print(f"Extraction error: {e}")
        return None
