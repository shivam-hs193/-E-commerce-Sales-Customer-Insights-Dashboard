# src/data_cleaning.py
# Usage: python src/data_cleaning.py
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def clean_orders():
    orders = pd.read_csv(BASE/'data/raw/ecommerce_orders_raw.csv', parse_dates=['Order_Date'])
    # Drop exact duplicates
    before = len(orders); orders = orders.drop_duplicates(); after = len(orders)
    print(f"Removed duplicates: {before-after}")

    # Handle missing values
    orders['Payment_Mode'] = orders['Payment_Mode'].fillna('Unknown')

    # Ensure dtypes
    orders['Quantity'] = orders['Quantity'].astype('int64')
    orders['Discount_Pct'] = orders['Discount_Pct'].astype('float64')

    # Feature engineering
    # Already present in raw, but recompute to ensure correctness
    orders['Gross_Revenue'] = (orders['Quantity'] * orders['Unit_Price']).round(2)
    orders['Discount_Amount'] = (orders['Gross_Revenue'] * orders['Discount_Pct']).round(2)
    orders['Net_Revenue'] = (orders['Gross_Revenue'] - orders['Discount_Amount']).round(2)
    orders['COGS'] = (orders['Quantity'] * orders['Unit_Cost']).round(2)
    orders['Profit'] = (orders['Net_Revenue'] - orders['COGS']).round(2)
    orders['AOV'] = (orders['Net_Revenue'] / orders['Quantity']).round(2)

    out = BASE/'data/processed/ecommerce_orders_clean.csv'
    orders.to_csv(out, index=False)
    print(f"Saved cleaned file to: {out}")

if __name__ == "__main__":
    clean_orders()
