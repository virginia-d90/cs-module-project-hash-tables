# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# create a list of letters from most -> least used
# create a dictionary of the number of times each letter occurs in the text
    #need to ignore special characters and spaces --> i think isalpha() will work
#sort dict in order of frequency
#overwrite values in dict to be the letters in the list

char_by_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

char_count = {}
decoded = {}

def crack_caesar(file):
    with open(file) as f:
        text = f.read()

    for char in text: #populate char_count
        if char.isalpha() == True:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse =True)

    index_counter = 0
    for key, val in sorted_char_count:
        decoded[key] = char_by_freq[index_counter]
        index_counter += 1

    decoded_text = ''

    for char in text:
        if char.isalpha() == False:
            decoded_text += char
            continue
        decoded_text += decoded[char]
    print(decoded_text)

    

crack_caesar('ciphertext.txt')


    