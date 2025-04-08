# load.py

import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Read config from environment
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 3306)),  # default port if not provided
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def save_to_db(price):
    """Save the transformed stock price into the MySQL database."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tatasteel_stock_prices (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    price FLOAT NOT NULL,
                    timestamp DATETIME NOT NULL
                );
            """)
            cursor.execute("INSERT INTO tatasteel_stock_prices (price, timestamp) VALUES (%s, %s)", (price, datetime.now()))
            connection.commit()
            print("✅ Stock price inserted successfully.")
    except Error as e:
        print(f"❌ Database error: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
