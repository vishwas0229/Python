import pickle
import random as nd
import string as st
from pathlib import Path

def loadData():
    try:
        if Path("data.dat").exists():
            with open("data.dat", "rb") as f:
                return pickle.load(f)
                
    except Exception as err:
        print(err)
    
    return []

def write(data):
    id = nd.choices(st.digits, k = 5)
    nd.shuffle(id)
            
    info = {
        'ID' : "".join(id),
        'Name' : input("Enter Name: "),
        'Age' : int(input("Enter Age: ")),
        'City' : input("Enter City: "),
        'Salary': int(input("Enter Salary: "))
    }
    
    data.append(info)
    
    with open("data.dat", "wb") as f:
        pickle.dump(data, f)
        
    print("=========================")
    print(f"Note Generated ID: {info["ID"]}")
    return "File written Successfull"
        
        
def read(data):
    
    id = input("Enter ID: ")
    
    empData = [i for i in data if i['ID'] == id]
    
    if not empData:
        print("Employee dosen't exist.")
        
    else:
        print("=====Employee Details=====")
        for i in empData[0]:
            print(f"{i} : {empData[0][i]}")

data = loadData()

print("1. Write\n2. Read")
ch = int(input("Enter your choice (1 or 2): "))
if ch == 1:
    print(write(data))
    
elif ch == 2:
    read(data)
    
else:
    print("Invalid Input")