textlist = ['banan', 'apple', 'rakieta', 'rower', 'rr', 'aaa', 'bbbbb']

for word in textlist:
    if len(word) > 2 and word[0] == word[len(word)-1]:
        print(word)

