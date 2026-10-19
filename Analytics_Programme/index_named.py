import pandas as pd
lst= [12,54,34,21,56,45,44,22,24,10]
index = [1,2,3,4,5,6,7,8,9,10]
print(pd.Series(lst))
print(pd.Series(lst,index = index))