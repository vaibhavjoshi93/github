A=[10,20,30,40,50]
n=len(A)
for i in range(1,n):
    A[i]=A[i]+A[i-1]
print("new list is",A)
