import numpy as np
import pandas as pd

data_list = [12, 15, 22, 18, 25, 30, 14, 20, 27, 19]

data_np = np.array(data_list)
data_pd = pd.Series(data_list)

print("Ungrouped Data List:", data_list)

data_range = np.max(data_np) - np.min(data_np)
print(f"\na) Range: {data_range}")

var_np = np.var(data_np, ddof=1)
var_pd = data_pd.var()

print(f"b) Variance (NumPy): {var_np:.2f}")
print(f"   Variance (Pandas): {var_pd:.2f}")

std_np = np.std(data_np, ddof=1)
std_pd = data_pd.std()

print(f"c) Standard Deviation (NumPy): {std_np:.2f}")
print(f"   Standard Deviation (Pandas): {std_pd:.2f}")
