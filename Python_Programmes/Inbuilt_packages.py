import math as m
import datetime as dt
import random as r

def dice():
    i = r.randint(1,6)
    print(f"Your random generated die number is {i}\n")

def square_root():
    i = int(input("Enter the number whose square root you want : "))
    print(f"Square root of the provede number is {m.sqrt(i)}\n")

def exponent():
    n = float(input("Enter the base : "))
    i = int(input("Enter the exponent : "))
    print(f"The result is {m.pow(n,i)}\n")

def current_datetime():
    now = dt.datetime.now()
    print("Current DateTime:", now) 

dice()
square_root()
exponent()
current_datetime()