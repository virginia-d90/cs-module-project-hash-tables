import random
#split() the text in words
#will need a couple of lists:
    #start words = words that start with a capital letter or "followed by a capital
    #end words = words that end with ".?!"
#create a dictionary
    #frequent follows = 
        #a word is the key
        #value will be a list of all words that immediately follow that word


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()


# TODO: analyze which words can follow other words
# Your code here
#for each word in words:
    #if start word
        #add to list
    #if end word 
        # add to list
    #if word is not not a key in the dictionary: 
        #make the word a key and the word at the next index a value
    #else the key exists
        #check if the word following is a value 
            #if yes?????
            #if no add value
start_words = []
end_words = []
frequency_dict = {}

for index,word in enumerate(words): #need enumerate to track the length of words list
    if word not in frequency_dict:
        if index < len(words) - 1:
            frequency_dict[word] = [words[index + 1]]
        else:#handles last word in list
            frequency_dict[word] = None #not sure if I need to set this to something else
    else:
        if index < len(words) -1:
            frequency_dict[word].append(words[index + 1])
    if word[0] == '"' and word[1].isupper() or word[0].isupper():
        start_words.append(word)
    if word[-1] in '.?!':
        end_words.append(word)

print(end_words)


# TODO: construct 5 random sentences
#probably a FOR loop with a range of 5
#choose a random start word
#check that the word isn't also a start word e.g House!
#add randomly chosen word from the start word frequent follows
#continue until a end word is chosen

for i in range(5):
    s = random.choice(start_words)

    if s not in end_words:
        next_word = random.choice(frequency_dict[s])
        s += " " + next_word

        while next_word not in end_words:
            next_word = random.choice(frequency_dict[next_word])
            s += " " + next_word
    print(s)


