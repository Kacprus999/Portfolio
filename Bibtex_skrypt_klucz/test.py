line='Article-Number = {{UNSP2}},\n'
artkey=''
x = line.split("Article-Number = {{")
x = x[1].split('}},\n')
iloscspac = line.count(' ')
if iloscspac > 0:
    x=x[0].split()
    for y in range(len(x)-1):
        x[y]+='space'
for y in x:
    artkey += y
print(artkey)
