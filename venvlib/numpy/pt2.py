import numpy as np
import pandas as pd

arr1 = np.array([
                [1, 2,  3],
                [4, 5, 6]
])

b = arr1.reshape(1, 6)

c = b.reshape(3, 2)

arr2 = np.array([
                [7, 8,  9],
                [10, 11, 12]
])



arr = np.array([1, 2, 3, 4, 5, 6])
arr = arr.reshape(3, 2)
append = np.array([10, 100])
C = arr + append 

C = C.transpose()

C = C.flatten()



data = {
    "height": [165, 170, 168, 172, 180],
    "weight": [55, 65, 58, 70, 80],
    "age": [21, 25, 23, 30, 35]
}

df = pd.DataFrame(data)
print(df)
print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Std Dev:\n", df.std())
print("Min:\n", df.min())
print("Max:\n", df.max())
print(df.describe())
print(df.corr())