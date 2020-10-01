import re
def word_count(s):
    # Your code here
    # s is a string
    # will return a dictionary where key = word and value = number of occurences
    # all words should be lowercase
    #ignore special characters >>> 
    counted = {}
    s = s.split()

    for word in s:
        word = "".join(char for char in word if char.isalpha() or char == "'").lower()

        if word == "":
            continue
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1
    return counted
   





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))