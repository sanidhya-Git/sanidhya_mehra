import numpy as np

a = np.array([1, 2, 3])

b = np.array([[4, 5, 6],
              [7, 8, 9]])

vertical = np.vstack([b, a])

a = np.array([10, 11])     
a = a.reshape(-1, 1)
horizontal = np.hstack([b, a])

print("Vertical Stack:")
print(vertical)

print("\nHorizontal Stack:")
print(horizontal)
