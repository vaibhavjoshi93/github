arr = [5, -1, -1, 1, 2, 3]
m=7
#print(len(arr))
a=[]
for i in range (len(arr)):
    if(arr[i] == -1):
        x=(arr[i-1] + 1) % m
        a.append(x)
    else:
        y=arr[i]
        a.append(y)

print(a)
