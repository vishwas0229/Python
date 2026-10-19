import numpy as np
list1=[16,4,14,21,96,45,94,22,24,98,55,64,54,34,21,56,45,44,22,75]
arr1 = np.array(list1).reshape(4,5)
print(f"The original matrix is\n{arr1}")
print(f"\n\nThe maximum value from each column is {np.max(arr1,axis=0)}\n")
print(f"The maximum value from each row is {np.max(arr1,axis=1)}")