import pandas as pd

df = pd.read_csv("data1.csv")
print("\n--- (a) Adding a New String Column ---")

df['Status'] = 'Pass'  
print(df)

print("\n--- (b) Removing Leading and Trailing Whitespace ---")
string_columns = df.select_dtypes(include=['object']).columns
for col in string_columns:
    df[col] = df[col].astype(str).str.strip()
print("\n",df,"\n")
df.to_csv("data1.csv", index=False)
print("\n[Success] The physical 'data1.csv' file has been updated and saved!")