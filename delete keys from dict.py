from collections import Counter
def common(ar1,ar2,ar3):
    ar1=Counter(ar1)
    print(ar1)
    ar2=Counter(ar2)
    ar3=Counter(ar3)
    intersection=dict(ar1.items()&ar2.items()&ar3.items())
    print(intersection)
    newlist=[]
    for (key,value) in intersection.items():
        for i in range(0,value):
            newlist.append(key) not in newlist
    print(newlist)

ar1 = [1, 5, 20, 20, 80, 80] 
ar2 = [6, 20, 20, 80, 80] 
ar3 = [3, 4, 20, 20, 80, 70, 80, 120]
common(ar1,ar2,ar3)
