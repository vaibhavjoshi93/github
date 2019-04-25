def isMonotonic(A,n):
    return (all(A[i]<=A[i+1] for i in range(n-1))) or (all(A[i]>=A[i+1] for i in range (n-1)))

A=[1,2,3,4]
n=len(A)
print(isMonotonic(A,n))
