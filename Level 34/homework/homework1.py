def find_short(s): #defining the function "find_short(s)"
    list1 = s.split(" ") # using the split method to turn the argument string into a list and a space as a seperator


    word_len = len(list1[0]) # declaring the variable that will store the shortest word of the "s" string (now list)
    for i in list1: # a for cycle to determine the shortest word of the "s" list
        if len(i) < word_len:
            word_len = len(i)
    
    # word_len = 3
    return word_len # returning the variable containing the shortest word's length
# use case:
print(find_short("bitcoin take over the world maybe who knows perhaps")) # result: 3 # shortest word: the