import pandas as pd

df = pd.read_csv('./sales_data.csv')

df[df['Quantity'] > 5]

# Look at Quantity column

# Compare each value to 5

# Keep rows where result is True

# No loops. No if statements. Vectorized logic.

df[(df['Region'] == 'East') & (df['Payment_Status'] == 'Paid')]

df['Total_Amount'].idxmax()

# What max gives
# The largest value.

# What idxmax gives
# The row position where the largest value lives.

# This does not return the value.
# It returns where the value is.

df.loc[df['Total_Amount'].idxmax()]
