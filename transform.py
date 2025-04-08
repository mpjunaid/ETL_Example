# transform.py

def clean_stock_price(price_text):
    try:
        return float(price_text.replace("₹", "").replace(",", "").strip())
    except ValueError:
        print("Transformation error: Invalid price format")
        return None
