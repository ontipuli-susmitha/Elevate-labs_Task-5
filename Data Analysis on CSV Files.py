import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load CSV File
# -------------------------------
# Replace 'sales_data.csv' with your actual file name
df = pd.read_csv("sales_data.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nShape of Dataset (Rows, Columns):", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())


# -------------------------------
# 2. Handle Missing Values
# -------------------------------
df = df.dropna()   # remove missing values
# df['Sales'].fillna(0, inplace=True)  # alternative method


# -------------------------------
# 3. Basic Data Analysis
# -------------------------------

# Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Sales by Product
sales_by_product = df.groupby('Product')['Sales'].sum()
print("\nSales by Product:")
print(sales_by_product)

# Sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:")
print(sales_by_region)

# Filter Example (Sales greater than 1000)
high_sales = df[df['Sales'] > 1000]
print("\nHigh Sales Records (>1000):")
print(high_sales)


# -------------------------------
# 4. Visualization
# -------------------------------

# Bar Chart - Sales by Product
plt.figure()
sales_by_product.plot(kind='bar')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Chart - Sales by Region
plt.figure()
sales_by_region.plot(kind='bar')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


# -------------------------------
# 5. Sales Trend (If Date Column Exists)
# -------------------------------
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    daily_sales = df.groupby('Date')['Sales'].sum()

    plt.figure()
    daily_sales.plot()
    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()


# -------------------------------
# 6. Additional Insights
# -------------------------------

print("\nAverage Sales:", df['Sales'].mean())
print("Maximum Sale:", df['Sales'].max())
print("Minimum Sale:", df['Sales'].min())

print("\nData Analysis Completed Successfully ✅")
