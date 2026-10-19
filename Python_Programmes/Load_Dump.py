import pickle 


def write():
    str = input("Enter string to write in the binary file : ")
    with open("File.dat","wb") as f:
        pickle.dump(str,f)
        
    return "File written Successfull"
        
        
def read():
    with open("File.dat","rb") as f:
        return pickle.load(f)
        

print("1. Write\n2. Read")
ch = int(input("Enter your choice (1 or 2): "))
if ch == 1:
    print(write())
    
elif ch == 2:
    print(read())
    
else:
    print("Invalid Input")
