def reverse(s):
    return s[::-1]
def checkcondition(s):
    value=reverse(s)
    if (s==value):
        return True
    return False

s="namana"
conditioncheck=checkcondition(s)

if conditioncheck==True:
    print("its Palindrom")

else:
    print("its not Palindrom")
    
