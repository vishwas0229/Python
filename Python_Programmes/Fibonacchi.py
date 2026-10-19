
def fib(num):
    
    if num == 1:
        return 0
        
    elif num == 2:
        return 1
    
    else:
        return fib(num - 1) + fib(num - 2)

num = int(input("Enter a number: "))
lit = [fib(i) for i in range(1, num + 1)]
print(lit)