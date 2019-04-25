A=[1,2,3,4,5,6,7]
evencount,oddcount=0,0
for i in range(len(A)):
    if A[i]%2==0:
        evencount+=1
    else:
        if A[i]%2!=0:
            oddcount+=1
print("even count is",evencount)
print("odd count is",oddcount)
    
