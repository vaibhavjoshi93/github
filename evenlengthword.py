def evenlenghword(newlist):
    emptylist=[]
    for i in newlist:
        if len(i)%2==0:
            emptylist.append(i)
    return emptylist

list1="this is python languag"
newlist=list1.split()
finalanswer=evenlenghword(newlist)
print(finalanswer)
