def numisprimeornot(n):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                print("the number",n,"is not prime")
                break
        else:
            print ("the number",n,"is prime")
n=6
check=numisprimeornot(n)
print(numisprimeornot)
