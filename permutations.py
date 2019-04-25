from itertools import permutations
def requiredvalues(str):
    value=permutations(str)
    for prem in list(value):
        print (''.join(prem))

str="abc"
requiredvalues(str)

