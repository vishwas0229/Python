def duplicate(list1, list2):
    dup = []
    for i in list1:
        for j in list2:
            if i == j:
                dup.append(i)
                
    return dup

l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 5, 6, 8]

print(duplicate(l1, l2))