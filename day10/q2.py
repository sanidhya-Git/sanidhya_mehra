import numpy as np
arr = np.random.randint(0, 10, (2, 3, 4))
print("Original shape:", arr.shape)
new = np.moveaxis(arr, 0, -1)
print("New shape after moveaxis:", new.shape)
