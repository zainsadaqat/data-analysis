import pandas as pd

df = pd.read_csv('./sales_data.csv')

df.groupby('Product')['Total_Amount'].sum()

# Step by step

# Split data by Product

# Select Total_Amount column

# Add values per group

# Output:

# One row per product

# One total per product