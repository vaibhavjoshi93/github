def multiplication(arr,n):
    mul=1
    for i in range(6):
        mul=mul*arr[i]
    return (mul)

arr=[100,10,5,25,35,14]
n=len(arr)
k=11
finalvalue=multiplication(arr,n)
answer=(finalvalue)%k
print(answer)
