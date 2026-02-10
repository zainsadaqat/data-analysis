import pandas as pd

df = pd.read_csv('./foodhub_order.csv')

print(df.shape)

# import numpy as np

# # (1×11) + (2×14) + (3×17)

# first_array = np.array([1, 2, 3])
# second_array = np.array([11, 14, 17])

# print(max(second_array))
# print(min(second_array))

# # print(sum(first_array * second_array))


# # scores = np.array([40, 60, 95, 31, 80])
# # passing_score = 50

# # print(scores > passing_score)


# # numpy_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# # regular_list = [10, 20, 30]
# # print(type(numpy_array))
# # print(type(regular_list))


# # b = np.array([11, 14, 17])

# # result = np.sum(a * b)
# # print(result)