with open("Test.txt","r") as f:
    fr = f.read()
    word = fr.split()
    count=0
    for i in word:
        count+= 1
    print(f"Number of words in the given files are : {count}")
