import os 
import random
import string
import pandas as pd

n = 10
display = [1, 4, 6]

if not os.path.exists("data.csv"):
    data = []
    for i in range(n):
        emp_id = random.choices(string.digits, k=5)
        info = {
            'ID': int("".join(emp_id)), 
            'NAME': input("Enter Name: "),
            'Age': int(input("Enter Age: ")),
            'Dept': input("Enter Department: "),
            'Salary': int(input("Enter Salary: "))
        }
        data.append(info)
    pd.DataFrame(data).to_csv("data.csv", index=False)

df = pd.read_csv("data.csv")


print("\nThe first five data records are:\n", df.head(5))
print("\nThe last five data records are:\n", df.tail(5))


print("\nThe data records of serial numbers 1, 4, 6 are:\n", df.iloc[[i-1 for i in display]])


df = df.rename(columns={'NAME': 'E_NAME'})
print("\nAfter renaming column:\n", df)


df['ID'] = df['ID'].astype(str)
df = df.rename(columns={'ID': 'E_ID'}) 
print("\nAfter changing ID to string:\n", df)
