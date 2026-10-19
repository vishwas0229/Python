
def pall_n(start, end):
    pallList = []
    for num in range(start, end + 1):
        
        if num < 10:
            continue
        
        if str(num) == str(num)[::-1]:
            pallList.append(num)
             
    return pallList
        
start = 1
end = 300

print(pall_n(start, end))