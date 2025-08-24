CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

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
