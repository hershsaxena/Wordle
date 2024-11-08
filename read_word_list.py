possible_words = []
file = open('words.txt', 'r')

for word in file:
    if word[-1:] == '\n':
        possible_words.append(word[0:-1])
    else:
        possible_words.append(word)

file.close()