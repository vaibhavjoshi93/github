minimum=int(input("the minimum number is:"))
maximum=int(input("the max number is"))

for Value in range(minimum,maximum+1):
    if Value>1:
        for i in range(2,Value):
            if (Value%i)==0:
                break
        else:
            print(Value)
