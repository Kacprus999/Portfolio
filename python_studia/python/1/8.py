f = open("test.txt")

text = f.read()
words = text.split()
print("number of words: ", len(words))
setofwords = set(words)


for x in setofwords:
    print("number of instances \" ",x," \" is equal to:", words.count(x))


f.close()
