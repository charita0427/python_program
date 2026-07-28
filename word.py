def match_word (word):
    ctr = 0
    lst = []
    for word in word: #this loop looks for words in the list
        if len(word) > 1 and word[0] == word [-1]: # says that the words must be greater than 1 letter and it first character = the last character
            ctr += 1 #increases the counter by 1 everytime it finds the matching word
            lst.append(word) #append means to add a single element to the list

    print("List of words with first and last number\n", lst)
    return ctr
count = match_word(['abc', 'cfc', 'opt', '444',])
print("The number of words which share the same first and last character are ", count)


    