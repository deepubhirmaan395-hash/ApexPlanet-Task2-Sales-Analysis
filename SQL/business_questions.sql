-- ApexPlanet Task 2
-- SQL Business Questions
-- Table: sales


-- Q1. Which category generated the highest total sales?

SELECT
    Category,
    SUM(Total_Sales) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;


-- Q2. What are the top 5 products by total sales?

SELECT
    Product,
    SUM(Total_Sales) AS Total_Sales
FROM sales
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 5;


-- Q3. Which cities generated the highest total sales?

SELECT
    City,
    SUM(Total_Sales) AS Total_Sales
FROM sales
WHERE City IS NOT NULL
  AND City <> ''
GROUP BY City
ORDER BY Total_Sales DESC;


-- Q4. What is the average order value?

SELECT
    ROUND(AVG(Total_Sales), 2) AS Average_Order_Value
FROM sales;


-- Q5. How many orders have a quantity greater than 5?

SELECT
    COUNT(*) AS Orders
FROM sales
WHERE Quantity > 5;


-- Q6. How do total sales compare by gender?

SELECT
    Gender,
    SUM(Total_Sales) AS Total_Sales
FROM sales
GROUP BY Gender
ORDER BY Total_Sales DESC;


-- Q7. How do total sales change month by month?

SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
    SUM(Total_Sales) AS Total_Sales
FROM sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Month;
