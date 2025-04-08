#!/bin/bash

VENV_DIR="/home/junaid/ETL_Example/venv"

# Step 1: Check for virtual environment
if [ ! -d "$VENV_DIR" ]; then
  echo "🔧 Virtual environment not found. Creating one..."
  python3 -m venv $VENV_DIR

  if [ $? -ne 0 ]; then
    echo "❌ Failed to create virtual environment."
    exit 1
  fi

  echo "✅ Virtual environment created."
fi

# Step 2: Activate virtual environment
source $VENV_DIR/bin/activate

# Step 3: Install requirements
if [ -f "/home/junaid/ETL_Example/requirements.txt" ]; then
  echo "📦 Installing dependencies..."
  pip install -r /home/junaid/ETL_Example/requirements.txt

  if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies."
    deactivate
    exit 1
  fi
else
  echo "⚠️ requirements.txt not found. Skipping dependency installation."
fi

# Step 4: Run the main ETL pipeline
echo "🚀 Running ETL pipeline..."
python /home/junaid/ETL_Example/main.py

# Step 5: Deactivate virtual environment
deactivate
echo "✅ Bash execution completed."
