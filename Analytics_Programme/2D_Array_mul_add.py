import numpy as np
list=[12,54,34,21,56,45,44,22,24,10,75,64,98,55,64,54]
list1=[16,4,14,21,96,45,94,22,24,98,55,64,54,34,21,56]
arr1 = np.array(list).reshape(4,4)
arr2 = np.array(list1).reshape(4,4)
print(f"Addition of the matrix :\n{arr1+arr2}")
print(f"\nProduct of the matrix :\n{arr1@arr2}")