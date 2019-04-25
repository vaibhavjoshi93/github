def firststring(string1,string2,n):
    for i in range (0,n):
        for j in range(0,5):
            if string2[j]==string1[i]:
                answer=print("Accepted")
                return answer
    answer="Not Accepted"
    return answer        

string1="gks"
string2="aeiou"
n=len(string1)
finalvalue=firststring(string1,string2,n)
#print(finalvalue)
                
