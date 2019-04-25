A=[1,2,3,4,5]
n=len(A)
max=max(A[0],A[1])
min=min(A[0],A[1])
for i in range(1,n):
    if A[i]>max:
        min=max
        max=A[i]
    else:
        if A[i]>min:
            min=A[i]
            
print("2nd largest is",min)


A.sort()
A.remove(-1)
max(A)
    
