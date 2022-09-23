textlist = ['banan', 'apple', 'rakieta','xor' ,'rower', 'rr', 'aaa', 'bbbbb','xobek']
xlist = []

for word in textlist:
    if word.startswith("x"):
        xlist.append(word)
        textlist.remove(word)
        
xlist.sort()
textlist.sort()

print(xlist+textlist)
