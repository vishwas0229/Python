import numpy as np
num = int(input("Enter what you want : "))
arr = np.array((1, 2, 3, 4, 5, 6))

for i in range(len(arr)):
    if num == arr[i]:
        print(f"index number of {num} is {i}.")
