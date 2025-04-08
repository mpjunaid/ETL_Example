# 🛠️ ETL Pipeline in Python

This project demonstrates a modular and beginner-friendly ETL (Extract, Transform, Load) pipeline in Python. It is designed to extract Tata Steel stock prices from the web, transform the data, and load it into a MySQL database.

The pipeline is split into three main components:

- **Extract:** Collects data using web scraping.
- **Transform:** Cleans and converts the data into a structured format.
- **Load:** Saves the cleaned data into a MySQL database.

The project uses:

- `requests` and `BeautifulSoup` for web scraping  
- `python-dotenv` to manage environment variables  
- `mysql-connector-python` to interact with the MySQL database

---

# 📄 File Explanations - ETL Pipeline in Python

This document provides a concise explanation of the purpose and role of each Python file used in the ETL pipeline project.

---

## `main.py`

**Role:**  
This is the main entry point for the ETL pipeline.

**Functionality:**
- Loads environment variables from `.env`
- Imports and calls the `extract`, `transform`, and `load` functions
- Handles any pipeline-level error handling or orchestration logic

---

## `extract.py`

**Role:**  
Responsible for the **Extract** step of the ETL pipeline.

**Functionality:**
- Uses `requests` to fetch the web page containing Tata Steel stock price
- Uses `BeautifulSoup` to parse and extract the stock price from HTML
- Returns the extracted price data to be processed in the transform step

---

## `transform.py`

**Role:**  
Handles the **Transform** step of the ETL process.

**Functionality:**
- Validates the extracted data (e.g., ensures it's a valid float or number)
- Formats or cleans the data if necessary
- Returns the cleaned and validated data ready to be inserted into the database

---

## `load.py`

**Role:**  
Handles the **Load** step of the ETL pipeline.

**Functionality:**
- Connects to a MySQL database using credentials from the `.env` file
- Creates a table `tatasteel_stock_prices` if it doesn't exist
- Inserts the transformed data into the database with a timestamp
- Closes the database connection safely

---

## 🖥️ `run_etl.sh`

**Purpose:**  
This is a shell script to automate the setup and execution of the ETL pipeline.

**What it does:**
- Checks if a Python virtual environment (`venv/`) exists.
- If not, it creates a new virtual environment.
- Activates the virtual environment.
- Installs all required Python packages listed in `requirements.txt`.
- Runs the main Python script (`main.py`) to start the ETL process.

**Usage:**
```bash
chmod +x run_etl.sh   # Make the script executable (run once)
./run_etl.sh          # Execute the script
```
---

## 🔐 .env

**Purpose:**  

Stores sensitive or environment-specific configuration values securely and separately from the source code.

Contents:
```bash
DB_HOST=localhost
DB_PORT=3306
DB_USER=airflow
DB_PASSWORD=airflow_password
DB_NAME=airflow
```