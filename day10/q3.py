import numpy as np
arr = np.array([[1, np.nan, 3], [4, 5, np.nan], [7, 8, 9]], dtype=float)
col = np.nanmean(arr, axis=0)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(col, inds[1])
print("Array after replacing NaNs with column averages:\n", arr)
