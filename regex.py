import re
def charinstring(string):
    regex=re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    if (regex.search(string)==None):
        print("Accepted")
    else:
        print("Not accepted")

string=('Geek"Geek')
charinstring(string)
