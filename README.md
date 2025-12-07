# ISM2411 Data Cleaning Project

## Overview
This project demonstrates cleaning a messy sales dataset using Python and Pandas. 
The goal was to standardize column names, handle missing values, remove invalid rows, and produce a clean CSV ready for analysis.

## Project Structure
ism2411-data-cleaning-copilot/
├── data/
│ ├── raw/ # Original messy CSV
│ │ └── sales_data_raw.csv
│ └── processed/ # Cleaned CSV output
│ └── sales_data_clean.csv
├── src/
│ └── data_cleaning.py # Main data cleaning script
├── README.md # Project overview
└── reflection.md # Reflection on using Copilot and data cleaning

## How to Run
1. Make sure Python 3.x is installed and you have Pandas:
```bash
pip install pandas
python src/data_cleaning.py
data/processed/sales_data_clean.csv
#The script standardizes column names to lowercase with underscores.
#It trims whitespace in text fields and converts all text to lowercase.
#Missing numeric values are handled and negative prices or quantities are removed.
#GitHub Copilot was used to generate initial function code, which was then modified to fit the dataset.
