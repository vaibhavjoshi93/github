def elementinlist(list):
    count=0
    for i in list:
        if (i==3):
            count=count+1
    return count
list=[1,2,3,4,5,3,3]
answer=elementinlist(list)
print("the answer is",answer)


#you can use list.count(X) method also
        
