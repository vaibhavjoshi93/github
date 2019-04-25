from difflib import get_close_matches
def closematches(pattern,word):
    print (get_close_matches(word,pattern))

pattern=['ape', 'apple', 'peach', 'puppy']
word = 'app'
closematches(pattern,word)

