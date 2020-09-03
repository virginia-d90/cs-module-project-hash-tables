#take in a string
#return string - minus any additional occurances of the word

#create an variable that is set to an empty string ---->> this is the output
#split the string into a list of words
#make the list of words keys in a dictionary 
#loop through each word in the list and check if it is a key in the dictionary
    #if key is not found add it to dictionary
    #also at the key to the result string 


def no_dups(s):

    no_dup_str = ""
    word_list = s.split()
    used_words = {}

    for word in word_list: #check each word 
        if word not in used_words: # see if word has been used
            used_words[word] = word # new word added to dictionary
            no_dup_str += word + " " # word added to final result with a space

    return no_dup_str.strip()#removes extra space at end of string
    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))