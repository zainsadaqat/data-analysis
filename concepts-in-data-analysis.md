# Concepts in Data Analysis

## Most Commonly Used Pandas Data Types (Dtypes)

### object	

Primarily used for text or mixed types. If a column contains strings or a mix of numeric and non-numeric values, pandas will default to object.

### int64	

For integer numbers. The default int64 (64-bit integer) is used unless a smaller, more memory-efficient type like int8, int16, or int32 is specified.

### float64	

For floating point numbers (decimals). Similar to integers, smaller types like float32 can be used for memory optimization.

### bool	

For boolean values (True/False).

### datetime64

Specific to dates and times, allowing for powerful time-series operations, formatting, and time zone adjustments.

### category	

Represents a finite list of text values (low cardinality data). This type is highly memory efficient and useful for data with a limited number of unique categories, like "US", "Canada", "Mexico" for a country column.

## Imputation 

Imputation in pandas is the process of replacing missing values (represented as NaN or None) in a DataFrame or Series with substitute values to ensure a complete dataset for analysis. 
The primary function for this in pandas is `fillna()`

### Core Pandas Imputation Methods

fillna(): Replaces NaN values with a specified static value or a dynamically calculated one.

####  Fill all missing values with a specific constant

```py
df.fillna(0, inplace=True) 
```

#### Fill missing values in a column with its mean

```py
df['column_name'].fillna(df['column_name'].mean(), inplace=True) 
```

#### Use median if data has outliers

```py
df['column_name'].fillna(df['column_name'].median(), inplace=True)
```

#### Use mode for categorical data

```py
df['categorical_col'].fillna(df['categorical_col'].mode()[0], inplace=True)
```

## df["column"].value_counts(normalize=True)

It returns the percentage (proportion) of each value relative to the total number of non-null elements.

### What it Means

`.value_counts()` (default): Returns counts (e.g., Apple: 10, Orange: 5).

`.value_counts(normalize=True)`: Returns proportions (e.g., Apple: 0.66, Orange: 0.33), where the sum of all values is 1.0.

Result: It turns counts into percentages of the whole.

## Unique()

The `unique()` method in pandas is used to find all the distinct values within a Series (a single column of a DataFrame) or any 1-D array-like object.

```py
import pandas as pd

# Sample DataFrame creation
data = {'Name': ['Alice', 'Bob', 'Alice', 'David', 'Bob'], 'Age': [25, 30, 25, 22, 30]}
df = pd.DataFrame(data)

# Find unique values in the 'Name' column
unique_names = df['Name'].unique()

print(unique_names)
# Output: ['Alice' 'Bob' 'David']
```
