#def removeelement(list,word,N):
 #   newlist=[]
  #  count=0
   # for i in list:
    #    if (i==word):
     #       count=count+1
      #      if count!=N:
       #         newlist.append(i)
        #else:
         #   newlist.append(i)
    #if (count==0):
     #   print("iteam not found")

    #else:
     #   print("newlist is",newlist)

def removeelement(list,word,N):
    count=0
    for i in range(0,len(list)):
        if list[i]==word:
            count=count+1
            if count==N:
                del (list[i])
                #return True
    return list       
            
list=["geeks","for","geeks"]
N=2
word="geeks"
Flag=removeelement(list,word,N)
#removeelement(list,word,N)
print(Flag)

#if Flag==True:
  #  print("newlist is:",list)
#if Flag==False:
 #   print("no items")

