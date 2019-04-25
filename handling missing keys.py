import collections
dict={}
dict=collections.defaultdict(lambda : 'key not found')
dict[1]='vaibhav'
dict['B']=2
print("the value of 1 is",dict[1])
print("the value of C is",dict['C'])
