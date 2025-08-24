# src/load_to_mysql.py

import pandas as pd
import mysql.connector

# Load cleaned data
df = pd.read_csv("data/processed/ecommerce_cleaned.csv")

# -------------------- Connect to MySQL --------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="ecommerce_db"
)
cursor = conn.cursor()

# -------------------- Create Table --------------------
create_table = """
CREATE TABLE IF NOT EXISTS sales (
    OrderID VARCHAR(20),
    CustomerID VARCHAR(20),
    CustomerName VARCHAR(255),
    ProductID VARCHAR(20),
    ProductName VARCHAR(255),
    Category VARCHAR(100),
    OrderDate DATE,
    ShipDate DATE,
    Sales FLOAT,
    Quantity INT,
    Profit FLOAT,
    ProfitMargin FLOAT
);
"""
cursor.execute(create_table)

# -------------------- Insert Data --------------------
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales (OrderID, CustomerID, CustomerName, ProductID, ProductName, Category, OrderDate, ShipDate, Sales, Quantity, Profit, ProfitMargin)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()
print("✅ Data loaded successfully into MySQL!")
