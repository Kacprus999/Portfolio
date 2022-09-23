file = open("plik.txt")
thisdict={}

for line in file:
    linesplit=line.split()
    thisdict[linesplit[0]] = linesplit[1]


print(thisdict)
file.close()
