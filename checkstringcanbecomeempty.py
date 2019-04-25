def checkforempty(input1,pattern):
    if len(input1)==0:
        print( "the string is empty")
    while(len(input1)!=0):
        index=input1.find(pattern)
        if (index==-1):
            return False
        input1=input1[0:index]+input1[index+len(pattern):]
    return True

if __name__ == "__main__": 
    input1 ='GEEGEEKSKS'
    pattern ='GEEKS'
    print(checkforempty(input1, pattern) )
    
