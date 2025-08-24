USE ecommerce_db;

-- 1. Top 10 Best-Selling Products
SELECT ProductName, SUM(Sales) AS TotalSales
FROM sales
GROUP BY ProductName
ORDER BY TotalSales DESC
LIMIT 10;

-- 2. Top Customers by Revenue
SELECT CustomerName, SUM(Sales) AS Revenue
FROM sales
GROUP BY CustomerName
ORDER BY Revenue DESC
LIMIT 10;

-- 3. Monthly Sales Trend
SELECT DATE_FORMAT(OrderDate, '%Y-%m') AS Month, SUM(Sales) AS TotalSales
FROM sales
GROUP BY Month
ORDER BY Month;

-- 4. Sales by Category
SELECT Category, SUM(Sales) AS TotalSales
FROM sales
GROUP BY Category
ORDER BY TotalSales DESC;

-- 5. Repeat Purchase Ratio
SELECT CustomerID,
       COUNT(DISTINCT OrderID) AS TotalOrders
FROM sales
GROUP BY CustomerID
HAVING TotalOrders > 1;
