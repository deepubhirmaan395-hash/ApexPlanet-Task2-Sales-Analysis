import pandas as pd
import matplotlib.pyplot as plt

# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load cleaned Excel dataset
df = pd.read_excel("ApexPlanet_Task1_Cleaned_Dataset(1).xlsx")

# 3. Basic dataset inspection
print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

# 4. Descriptive statistics
numeric_cols = ["Age", "Quantity", "Unit_Price", "Total_Sales"]
print("\nDescriptive statistics:")
print(df[numeric_cols].describe())

# 5. Categorical analysis
for col in ["Gender", "City", "Product", "Category"]:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())

# 6. Age distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Age"].dropna(), bins=10)
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.title("Age Distribution")
plt.tight_layout()
plt.show()

# 7. Total sales distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Total_Sales"].dropna(), bins=15)
plt.xlabel("Total Sales")
plt.ylabel("Number of Orders")
plt.title("Total Sales Distribution")
plt.tight_layout()
plt.show()

# 8. Sales by category
category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
plt.bar(category_sales.index.astype(str), category_sales.values)
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Total Sales by Category")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

# 9. Sales by gender
gender_sales = df.groupby("Gender")["Total_Sales"].sum()

plt.figure(figsize=(7, 5))
plt.bar(gender_sales.index.astype(str), gender_sales.values)
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.title("Total Sales by Gender")
plt.tight_layout()
plt.show()

# 10. Top 10 products by sales
product_sales = (
    df.groupby("Product")["Total_Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10, 5))
plt.bar(product_sales.index.astype(str), product_sales.values)
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Top 10 Products by Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
