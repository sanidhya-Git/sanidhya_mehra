import numpy as np

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

arr2 = np.array([[9, 8, 7],
                 [6, 5, 4],
                 [3, 2, 1]])

print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

print("\n--- Max and Min ---")
print("Max value in arr1:", np.max(arr1))
print("Min value in arr1:", np.min(arr1))


print("\n--- Shape ---")
rows, cols = arr1.shape
print("Rows:", rows)
print("Columns:", cols)


print("\n--- Element Selection ---")
print("Row 1 (second row):", arr1[1])
print("Column 2 (third column):", arr1[:, 2])
print("Element at (0, 1):", arr1[0, 1])


print("\n--- Summation ---")
print("Total sum:", np.sum(arr1))
print("Sum by rows:", np.sum(arr1, axis=1))
print("Sum by columns:", np.sum(arr1, axis=0))

print("\n--- Arithmetic Operations ---")
print("Addition:\n", arr1 + arr2)
print("Subtraction:\n", arr1 - arr2)
print("Multiplication (element-wise):\n", arr1 * arr2)
print("Division (element-wise):\n", arr1 / arr2)


np.seterr(divide='ignore', invalid='ignore')
