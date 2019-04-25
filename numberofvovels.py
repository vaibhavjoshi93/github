def alphainstring(string1,vowels):
    count=0
    for alphabet in string1:
        if alphabet in vowels:
            count=count+1
    print (count)

string1="geeks"
vowels="aeiou"
alphainstring(string1,vowels)
