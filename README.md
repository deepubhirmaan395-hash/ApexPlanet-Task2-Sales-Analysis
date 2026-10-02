# ApexPlanet Task 2 – Sales Data Analysis & Business Intelligence

## Project Overview

This project is part of my ApexPlanet internship Task 2.

The objective of this project is to analyze a cleaned sales dataset using Python, SQL, Exploratory Data Analysis (EDA), multivariate analysis, correlation analysis, and a static dashboard.

The project focuses on understanding sales performance, customer behavior, product performance, category performance, and monthly sales trends.

---

## Dataset

The dataset contains **1,000 sales records and 13 columns**.

### Main Columns

- Order_ID
- Order_Date
- Customer_ID
- Customer_Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit_Price
- Total_Sales
- Original_Order_ID

---

##  Python – Exploratory Data Analysis

Python was used for:

- Dataset inspection
- Missing value analysis
- Descriptive statistics
- Categorical analysis
- Data visualization
- Univariate analysis
- Multivariate analysis
- Correlation analysis

### Visualizations

- Age Distribution
- Total Sales Distribution
- Sales by Category
- Sales by Gender
- Top Products by Sales
- Age vs Total Sales
- Quantity vs Total Sales
- Unit Price vs Total Sales
- Correlation Heatmap
- Pair Plot

---

## SQL Business Analysis

The cleaned dataset was imported into MySQL using the table:

`sales`

SQL was used to answer business questions using filtering, aggregation, grouping, sorting, and date-based analysis.

### Business Questions

1. Which category generated the highest total sales?
2. What are the top 5 products by total sales?
3. Which cities generated the highest total sales?
4. What is the average order value?
5. How many orders have quantity greater than 5?
6. How do total sales compare by gender?
7. How do total sales change month by month?

---

##  Multivariate Analysis & Correlation

Multivariate analysis was performed to understand relationships between numerical variables.

### Scatter Plots

- Age vs Total Sales
- Quantity vs Total Sales
- Unit Price vs Total Sales

### Correlation Analysis

A correlation heatmap was created for the numerical variables:

- Age
- Quantity
- Unit_Price
- Total_Sales

A pair plot was also created to explore relationships between multiple numerical variables.

---

## Static Sales Performance Dashboard

A static Sales Performance Dashboard was created using the insights obtained from the EDA and SQL analysis.

### Dashboard KPIs

- Total Sales: ₹13.94 Cr
- Total Orders: 1,000
- Average Order Value: ₹139,399
- Top Category: Electronics

### Dashboard Visualizations

- Category-wise Sales
- Gender-wise Sales
- Top 5 Products
- Monthly Sales Trend

---

##  Key Insights

### Category Performance

Electronics generated the highest total sales among the categories in the dataset.

### Gender Analysis

Sales associated with male customers were slightly higher than sales associated with female customers.

### Product Performance

Laptop, Mobile and Book were among the products with the highest total sales.

### Sales Distribution

Most orders are concentrated in the lower sales range, while fewer orders have very high sales values.

* Monthly Sales

Monthly sales varied throughout the analyzed period.

---

* Tools & Technologies

- Python
- Pandas
- Matplotlib
- MySQL
- SQL
- Microsoft Excel
- PowerPoint
- GitHub

---

 * Project Structure

```text
ApexPlanet-Task2-Sales-Analysis
│
├── README.md
│
├── ApexPlanet_Task2_Step1
│   ├── task2_step1_eda.py
│   ├── descriptive_statistics.csv
│   ├── missing_values_report.csv
│   ├── categorical_analysis.xlsx
│   └── EDA charts
│
├── SQL
│   └── business_questions.sql
│
├── Multivariate Analysis
│   ├── Age vs Total Sales
│   ├── Quantity vs Total Sales
│   ├── Unit Price vs Total Sales
│   ├── Correlation Heatmap
│   └── Pair Plot
│
└── ApexPlanet_Static_Sales_Dashboard.pptx

Conclusion
This project helped me practice Exploratory Data Analysis, SQL business analysis, data visualization, multivariate analysis, correlation analysis, and dashboard creation.
The analysis provides a visual and analytical overview of sales performance and demonstrates the use of Python and SQL for extracting meaningful insights from sales data.

Author
Deepanshu Bhirmaan
BCA – SGT University, 2026
Interested in Data Analytics and Data Science.
