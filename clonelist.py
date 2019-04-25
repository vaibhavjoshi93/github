def clonealist(list):
    newlist=list[:]
    return newlist

list=[1,2,3]
ans=clonealist(list)
print(ans)


def clonelist(list):
    newlist=[]
    newlist.extend(list)
    return newlist

