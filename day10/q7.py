from scipy import stats
import numpy as np
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
avg = (arr1 + arr2) / 2
print("Average of NumPy arrays:\n", avg)

arr_2d_1 = np.random.randint(0, 100, (3, 3))
arr_2d_2 = np.random.randint(0, 100, (3, 3))
combined = np.concatenate((arr_2d_1.flatten(), arr_2d_2.flatten()))
mean = np.mean(combined)
median = np.median(combined)
mode = stats.mode(combined, keepdims=True)[0]
print("Mean:", mean, "Median:", median, "Mode:", mode)
