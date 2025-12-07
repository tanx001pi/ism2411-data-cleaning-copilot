"""
data_cleaning.py
Purpose:
    Loads messy sales data, cleans it, and writes cleaned output to data/processed.
"""

import pandas as pd

# Copilot-assisted function
def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

# Copilot-assisted function
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

# Handles missing numeric values
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "price" in df.columns and "quantity" in df.columns:
        df = df.dropna(subset=["price", "quantity"], how="all")
    num_cols = df.select_dtypes(include="number").columns
    df[num_cols] = df[num_cols].fillna(0)
    return df

# Removes negative values
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convert price column to numeric first
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Check first few values and type
    print(df["price"].head(10))
    print(df["price"].dtype)

    # Remove rows with missing price
    df = df.dropna(subset=["price"])

    # Remove negative prices
    df = df[df["price"] >= 0]

    # Remove negative quantities if column exists
    if "quantity" in df.columns:
        df = df[df["quantity"] >= 0]

    return df


if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    # Load raw data
    df_raw = load_data(raw_path)
    print("Columns in CSV:", df_raw.columns)

    # Clean column names
    df_clean = clean_column_names(df_raw)

    # Strip whitespace from text fields
    for col in df_clean.select_dtypes(include="object").columns:
        df_clean[col] = df_clean[col].str.strip()

    # Handle missing numeric values
    df_clean = handle_missing_values(df_clean)

    # Remove invalid rows (negative prices/quantities)
    df_clean = remove_invalid_rows(df_clean)

    # Save cleaned CSV
    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())
