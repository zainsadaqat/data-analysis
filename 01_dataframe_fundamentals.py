import pandas as pd

df = pd.read_csv('./foodhub_order.csv')

# print(df.head())

# print(df.columns)

# print(df['restaurant_name'])

print(df[df['restaurant_name'] == 'Tortaria'])

# What this does

# Checks each row

# Compares Product value to 'Laptop'

# Produces True or False per row

# “Keep only the rows where the condition is True.”