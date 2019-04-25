def Nlargestelements(A,N):
    for i in range(0,N):
        max=0
        for j in range(len(A)):
            if A[j]>max:
                max=A[j]
        A.remove(max)
        B.append(max)
    print("the new list is",B)

A=[1,2,3,4]
B=[]
N=2
finallist=Nlargestelements(A,N)
