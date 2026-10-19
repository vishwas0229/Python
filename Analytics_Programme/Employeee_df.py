import pandas as pd
import random as np
import string as st
import os 
n=2
data=[]
display=[2]



if not os.path.exists("data.csv"):
    for i in range(0,n):
        id = np.choices(st.digits, k = 5)
        np.shuffle(id)
    
        info = {
                'ID' : "".join(id),
                'Name' : input("Enter Name : "),
                'Age' : int(input("Enter Age : ")),
                'Dept' : input("Enter Department : "),
                'Salary': int(input("Enter Salary : "))
            }
        data.append(info)
    df = pd.DataFrame(data)
    df.to_csv("data.csv", index = False)
def show_5_data():
    count = 0
    while count < 2:
        df=pd.read_csv("data.csv")
        print([x.item() if hasattr(x, 'item') else x for x in df.iloc[count]])
        count += 1
def show_given_data(): 
    for i in display:
        df=pd.read_csv("data.csv")
        print([x.item() if hasattr(x, 'item') else x for x in df.iloc[i-1]]) 
show_5_data()
show_given_data()



