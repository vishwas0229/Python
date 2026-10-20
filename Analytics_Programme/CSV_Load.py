import pandas as pd
data = {"Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["John Doe", "Jane Smith", "Alex Jones", "Emily Brown", "Michael Green"],
    "Department": ["IT", "HR", "Finance", "Marketing", "Operations"],
    "Salary": [75000, 62000, 81000, 58000, 69000]}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
print(f"Dataset successfully created and exported to '{"data.csv"}'\n")


exported_data = pd.read_csv("data.csv")
print("--- Displaying Data ---")
print(exported_data.to_string(index=False))
