import pandas as pd
import os

data = {
    'Name' : ['Jhon', 'Peter', 'Linda', 'Anna'],
    'Age' : [28, 37, 49, 42],
    'City' : ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}


if not os.path.exists("data.csv"):
    pdf = pd.DataFrame(data)
    pdf.to_csv("data.csv", index = False)
    print("CSV fie created successfully!")


df=pd.read_csv("data.csv")
print(df.to_string(index = False))