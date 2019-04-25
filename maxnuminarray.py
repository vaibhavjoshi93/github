def maxinarray(arr,n):
    maximum=arr[0]
    for i in range(1,n):
        if arr[i]>maximum:
            maximum=arr[i]
    return maximum
arr=[5,7,9,15,1]
n=len(arr)
maximum=maxinarray(arr,n)
print(maximum)
