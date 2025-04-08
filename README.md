🛠️ ETL Pipeline in Python

This project demonstrates a modular and beginner-friendly ETL (Extract, Transform, Load) pipeline in Python. It is designed to extract Tata Steel stock prices from the web, transform the data, and load it into a MySQL database.

The pipeline is split into three main components:

Extract: Collects data using web scraping.

Transform: Cleans and converts the data into a structured format.

Load: Saves the cleaned data into a MySQL database.

The project uses:

requests and BeautifulSoup for web scraping

python-dotenv to manage environment variables

mysql-connector-python to interact with the MySQL database

🚀 How to Run the Project

1. Clone the Repository

git clone https://github.com/yourusername/your-etl-project.git
cd your-etl-project

2. Setup Environment Variables

Create a .env file in the root directory:

DB_HOST=localhost
DB_PORT=3306
DB_USER=airflow
DB_PASSWORD=airflow_password
DB_NAME=airflow

3. Run the Shell Script

Use the provided shell script run_etl.sh which will:

Check for an existing virtual environment or create one

Install dependencies from requirements.txt

Activate the environment

Run the ETL pipeline using main.py

Make the script executable:

chmod +x run_etl.sh

Run the script:

./run_etl.sh

🕒 Automate with Crontab

To schedule automatic execution of the ETL job:

1. Find Absolute Path to Script

pwd

2. Open Crontab

crontab -e

3. Add the Job

To run the script every day at 9 AM:

0 9 * * * /bin/bash /full/path/to/your/project/run_etl.sh >> /full/path/to/your/project/log.txt 2>&1

This ensures:

Script runs daily

Logs are stored in log.txt

📦 Requirements

Install dependencies manually with:

pip install -r requirements.txt

Dependencies include:

requests

beautifulsoup4

mysql-connector-python

python-dotenv

📁 File Descriptions

extract.py: Scrapes the Tata Steel stock price from Google Finance using BeautifulSoup.

transform.py: Processes and validates the scraped data to ensure it's in a usable format.

load.py: Connects to the MySQL database using credentials from .env and inserts the transformed data.

config.py (optional): Used when not using .env to store configuration parameters.

main.py: Orchestrates the full ETL process by calling extract, transform, and load steps. Also handles environment setup.

requirements.txt: Lists the required Python libraries for the project.

run_etl.sh: Shell script that sets up the virtual environment, installs dependencies, and runs the ETL pipeline.

.env: Contains sensitive configuration values like database connection details (not committed to version control).