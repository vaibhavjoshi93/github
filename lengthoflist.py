def lenoflist(list,n):
    counter=0
    for i in range(n):
        counter=counter+1
    return counter
list=[1,2,3,4]
n=len(list)
finalans=lenoflist(list,n)
print(finalans)
