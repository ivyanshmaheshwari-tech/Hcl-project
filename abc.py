# Ivyansh Maheshwari 
# Food Delivery Operations Analytics
# First Semester B.Tech Project

import numpy as np
import pandas as pd

# Step 1: Load the dataset
data = pd.read_csv("food_delivery.csv")

print("FOOD DELIVERY DATASET")
print("---------------------")

# Step 2: Display first five rows
print("\nFirst 5 records:")
print(data.head())

# Step 3: Display dataset information
print("\nDataset Information:")
print(data.info())

# Step 4: Check number of rows and columns
print("\nShape of Dataset:")
print(data.shape)

# Step 5: Check column names
print("\nColumn Names:")
print(data.columns)

# Step 6: Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Step 7: Basic statistical information
print("\nStatistical Summary:")
print(data.describe())

# Step 8: Calculate revenue for each order
data["Calculated_Revenue"] = (
    data["Quantity"] * data["Price_Per_Item"]
)

print("\nRevenue Calculation:")
print(data[["Order_ID", "Quantity", "Price_Per_Item",
            "Revenue", "Calculated_Revenue"]])

# Step 9: Verify supplied revenue
data["Revenue_Status"] = np.where(
    np.isclose(data["Revenue"], data["Calculated_Revenue"]),
    "Correct",
    "Incorrect"
)

print("\nRevenue Verification:")
print(data[["Order_ID", "Revenue",
            "Calculated_Revenue", "Revenue_Status"]])

# Step 10: Display incorrect revenue records
incorrect_data = data[data["Revenue_Status"] == "Incorrect"]

print("\nOrders with Incorrect Revenue:")
print(incorrect_data)

# Step 11: Count correct and incorrect records
print("\nRevenue Verification Result:")
print(data["Revenue_Status"].value_counts())

# Step 12: Calculate total actual revenue
total_revenue = data["Calculated_Revenue"].sum()

print("\nTotal Calculated Revenue:", total_revenue)

# Step 13: Save the final result
data.to_csv("food_delivery_analysis.csv", index=False)

print("\nAnalysis completed successfully!")
print("Final data saved in food_delivery_analysis.csv")
