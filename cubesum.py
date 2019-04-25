def cubesofnumbers(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+pow(i,3)
    return sum
n=3
finalsum=cubesofnumbers(n)
print("the cube sum of",n,"is",finalsum)
