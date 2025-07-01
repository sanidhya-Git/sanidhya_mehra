import numpy as np
A = np.array([[1, -2, 3], [-1, 3, -2], [2, -5, 5]])
b = np.array([9, -6, 17])
x = np.linalg.solve(A, b)
print("Solution using linalg.solve:\n", x)


A_inv = np.linalg.inv(A)
x_inv = A_inv.dot(b)
print("Solution using inverse matrix method:\n", x_inv)
