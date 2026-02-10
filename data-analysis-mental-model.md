# Data Analysis Mental Model

## The Core Problem Pandas Solves

Real-world data comes as tables. Python natively does not handle tables well.

Lists are one-dimensional.

Dictionaries are key-value, not row-based.

Nested structures get messy fast.

Pandas exists to represent tabular data and perform vectorized operations on it.

## What a CSV Actually Is

A CSV is just text.

```.csv
Order_ID,Product,Quantity,Total_Amount
1,Laptop,2,2400
2,Keyboard,5,500
```

Key points to drill:

Each line = one record (row)

Commas separate fields (columns)

Everything is a string until parsed

Python sees this as raw text unless structured

Mental model:

CSV = text → rows → columns → values

## Data Before Pandas

How ugly this is without pandas.

```py
import csv

rows = []
with open('sales.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)
```

- Now Filter laptops

- Sum revenue

- Group by product

You will immediately feel the pain.

Pandas exists to eliminate this boilerplate.

## What is a DataFrame

A DataFrame is a 2D table with:

Rows = records

Columns = labeled arrays (Series)

Index = row labels

Key sentence to repeat:

A DataFrame is a dictionary of columns, not a list of rows.

This single sentence explains df['Column'].

## Why `df['Column_Name']` Exists

- df is the table

- df['Product'] means:

“Give me the entire column named Product”

What it returns:

- A Series

- A 1D labeled array

- Same length as the DataFrame

Show:

- type(df['Product'])

Then:

- df['Product'] == 'Laptop'

### Explain

This produces a boolean mask

One True/False per row

Then:

- df[df['Product'] == 'Laptop']

OR

- df[df['restaurant_name'] == 'Klong']

### Explain in words:

- “Keep rows where the mask is True”

- This is the single most important pandas concept.

## What is Series in Pandas?

A Pandas Series is a one-dimensional labeled array capable of holding data of any type (integers, strings, floating-point numbers, Python objects, etc.).

It is a fundamental data structure in the Pandas library, similar to a single column in a spreadsheet or a Python list with an attached index.

1D Data Structure: A Series is a one-dimensional data structure, unlike a DataFrame which is two-dimensional.

## Filtering as Logic, Not Syntax

```py
df[(df['Region'] == 'East') & (df['Payment_Status'] == 'Paid')]
```

Look at Region column

Check which rows are East

Look at Payment_Status column

Check which rows are Paid

Keep rows where both conditions are true

No pandas magic. Just boolean algebra.

## GroupBy: Split → Apply → Combine

Split data into groups

Apply a calculation per group

Combine results

```py
df.groupby('Product')['Total_Amount'].sum()
```

- groupby('Product') → buckets

- ['Total_Amount'] → select what to calculate

- .sum() → aggregate

GroupBy does nothing until you aggregate.

## Commonly used aggregate functions in pandas include:

### Statistical Functions

- mean(): Computes the average of the values.
- median(): Calculates the middle value.
- mode(): Returns the most common value(s).
- std(): Computes the standard deviation.
- var(): Computes the variance.
- skew(): Computes the unbiased skew.
- kurt(): Computes the kurtosis.
- sem(): Computes the standard error of the mean.
- quantile(): Returns values at the specified quantile(s).

### Mathematical Functions

- sum(): Computes the sum of values.
- prod(): Computes the product of values.
- min(): Finds the minimum value.
- max(): Finds the maximum value.
- abs(): Computes the absolute value (though often used in transform or apply).
- Counting and Positional Functions
- count(): Counts the number of non-null values.
- size(): Computes the group sizes (includes NaN values).
- nunique(): Counts the number of unique values.
- first(): Returns the first entry of each group.
- last(): Returns the last entry of each group.
- idxmin(): Returns the index of the minimum value.
- idxmax(): Returns the index of the maximum value.

## Columns as Data, Not Metadata

```py
df['High_Value'] = df['Total_Amount'] > 1000
```

Take `Total_Amount` column

Apply condition to every row

Store result as a new column

Explain why boolean is better than Yes/No strings:

Counts faster

Filters faster

Mathematical operations possible

## Refactor Your Existing Files (Important)

Your current files should be renamed and reordered:

### 01_dataframe_fundamentals.py

- read_csv

- df.head()

- df.columns

- df['Column']

- boolean masks

### 02_filtering_logic.py

- single condition

- multiple conditions

- idxmax explanation

### 03_groupby_mechanics.py

- sum, mean, size

- sorting

- idxmax vs head

### 04_analytics_cases.py

- your advanced practice file

## Pandas pipelines always follow this order

- Select columns

- Filter rows

- Group rows

- Aggregate values

- Sort results

- Slice output
