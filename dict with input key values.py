def allAnagram(input1): 
      
    # empty dictionary which holds subsets  
    # of all anagrams together 
    dict = {} 
  
    # traverse list of strings 
    for strVal in input1: 
          
        # sorted(iterable) method accepts any  
        # iterable and rerturns list of items 
        # in ascending order 
        key = ''.join(sorted(strVal))
        print("keyos:",key)
          
        # now check if key exist in dictionary 
        # or not. If yes then simply append the   
        # strVal into the list of it's corresponding  
        # key. If not then map empty list onto 
        # key and then start appending values 
        if key in dict.keys():
            print("key is",key)
            dict[key].append(strVal) 
        else: 
            dict[key] = [] 
            dict[key].append(strVal) 
  
     # traverse dictionary and concatenate values  
     # of keys together 
     #output = ""
  
# Driver function 
if __name__ == "__main__": 
    input1=['cat', 'dog', 'tac', 'god', 'act'] 
    print (allAnagram(input1)) 
