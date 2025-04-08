# main.py

import subprocess
import sys
import os

from extract import fetch_stock_data
from transform import clean_stock_price
from load import save_to_db

def main():
    raw_price = fetch_stock_data()
    if raw_price:
        print("✅ Data Extraction Successfull")
        cleaned_price = clean_stock_price(raw_price)
        if cleaned_price is not None:
            print("✅ Data Transformation Successfull")
            save_to_db(cleaned_price)
        else:
            print("❌  Data Transformation Failed")
    else:
        print("❌ Data Extraction failed")

if __name__ == "__main__":
    main()
