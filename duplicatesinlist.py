def duplicates(string1):
    a=[]
    for i in range(0,n):
        k=i+1
        for j in range(k,n):
            if string1[i]==string1[j] and string1[i] not in a:
                a.append(string1[i])    
    return a

string1="geeksforgeeks"
n=len(string1)
print(duplicates(string1))
