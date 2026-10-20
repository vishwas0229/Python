import os 
import random
import string
import pandas as pd

n = 20

if not os.path.exists("data1.csv"):
    data = []
    for i in range(n):
        erl_id = random.choices(string.digits, k=5)
        info = {
            'Enrol_No.': int("".join(erl_id)), 
            'NAME': input("Enter Name : "),
            'Age': int(input("Enter Age : ")),
            'Marks': int(input("Enter Marks : "))
        }
        data.append(info)
    pd.DataFrame(data).to_csv("data1.csv", index=False)


def analysing_data_display(df):
    print("\n--- (a) Data Information Summary ---")
    df.info()
    print("\nDescriptive Statistics:\n", df.describe())

def replace_missing(df):
    print("\n--- (b) Replacing Missing Values in 'NAME' ---")
    df['NAME'] = df['NAME'].fillna('Unknown')
    print(df)

def clean_rows(df):
    print("\n--- (c) Dropping Rows with Remaining Missing/Blank Values ---")
    f = df.dropna()
    print(f)

def clean_duplicates(df):
    print("\n--- (d) Dropping Duplicates based on Enrol_No. ---")
    f = df.drop_duplicates(subset=['Enrol_No.'], keep='first')
    print(f)
df = pd.read_csv("data1.csv")
analysing_data_display(df)
replace_missing(df)
clean_rows(df)
clean_duplicates(df)