#!/bin/bash

# Check if Python 3.13+ is installed
if ! command -v python &> /dev/null
then
    echo "Python is not installed or not available in PATH."
    exit 1
fi

# Create a virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source ./venv/bin/activate

# Install dependencies
echo "Installing requirements..."
if [ ! -f requirements.txt ]; then
    echo "Error: requirements.txt not found in the current directory!"
    exit 1
fi
pip3 install -r requirements.txt

echo "Environment setup completed successfully."
