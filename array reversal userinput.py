def reversal(arr,start,end):
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1
    return arr

value=input("please enter string:")
finalvalue=value.split()
length=len(finalvalue)

if length==1:
    finalvalue=list(value)
    start=0
    n=len(finalvalue)
    end=n-1
    finalarry=reversal(finalvalue,start,end)
    example=''.join(finalarry)
    print(example)

if length>1:
    start=0
    n=len(finalvalue)
    end=n-1
    finalarry=reversal(finalvalue,start,end)
    example=''.join(finalarry)
    print(example)
