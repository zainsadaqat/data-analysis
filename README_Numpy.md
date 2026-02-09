# Numpy

## NumPy is a library for working with many numbers at once.

- Python by itself is good at handling:

- one number

- one list

- one decision at a time

## NumPy is built for:

- thousands or millions of numbers

- fast calculation

- structured numeric data

## Core idea:

NumPy replaces slow Python loops with fast math on entire collections.

## Why NumPy exists

Problem with normal Python lists:

```py
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    result.append(n * 2)
```

This is:

- verbose

- slow at scale

- error-prone

NumPy solution:

```py
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])
result = numbers * 2
```

Same logic. Less code. Faster execution.

## When to use NumPy?

### Use NumPy when

- working with numeric data

- doing calculations

- preparing data for ML models

- handling matrices, vectors, scores, measurements

### Do not use NumPy for

- text-heavy data

- small scripts with no math

- simple control-flow program

### Rule:

If data is numeric and repetitive → NumPy

## What is a NumPy array

### A NumPy array is

- a container of same-type numbers

- stored in memory efficiently

- supports math directly

### Compare

Python list:

[1, 2, 3, 4]

NumPy array:

array([1, 2, 3, 4])

### Key difference

list → general-purpose

array → numeric-only, optimized

## Basic operations

```py
a = np.array([10, 20, 30])

print(a + 5)
print(a * 2)
print(a - 3)
```

What’s happening:

operation applied to every element

no loop written

no condition needed

NumPy writes loops for you internally.

## Comparison operations (connect to if-else)

```py
scores = np.array([45, 67, 89, 32])

print(scores > 50)
```

Output:

[False True True False]

### Explain:

result is an array of True/False

same comparison operator as Python

applied element-by-element

## Practical example (exam scores)

Scenario: analyze student exam scores.

scores = np.array([45, 67, 89, 32, 76])

print("All scores:", scores)
print("Passed:", scores >= 50)
print("Average score:", scores.mean())
print("Highest score:", scores.max())
print("Lowest score:", scores.min())

Explain step-by-step:

array stores scores

comparisons check pass/fail

.mean(), .max(), .min() are built-in numeric operations

No math theory. Only meaning.

## Why this matters for AI / ML

- ML models do not accept Python lists

- They accept NumPy arrays

- NumPy is the language of data underneath Pandas, scikit-learn, TensorFlow

### Mental model:

- Python teaches logic
- NumPy teaches data
- ML consumes NumPy

## Example of one million numbers, one operation, instant result

```py
import numpy as np

# create 1,000,000 numbers
numbers = np.arange(1_000_000)

# add 10 to every number
result = numbers + 10

print(result[:10])      # first 10 values
print(result[-10:])     # last 10 values
```
