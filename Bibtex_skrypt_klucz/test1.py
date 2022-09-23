import re
line='Booktitle = {{PROCEEDINGS OF THE ASME 38TH INTERNATIONAL CONFERENCE ON OCEAN, OFFSHORE   AND ARCTIC ENGINEERING, 2019, VOL 3}},\n'
bookkey=''
x = line.split("Booktitle = {{")
x = x[1].split('}},\n')
x[0]=x[0].lower()
x[0]=x[0].title()
x = x[0].split()
x = ' '.join(x)
x = x.replace('And', 'and')
x = x.replace('With', 'with')
x = x.replace('\&', 'and')
x = x.replace('Of', 'of')
x = x.replace('On', 'on')
x = x.replace('-', ' ')
x = re.sub(r'[0-9]*','',x)
x = re.sub(r'[0-9]ST*','',x)
x = re.sub(r'[0-9]TH*','',x)        
x = re.sub(r'[0-9]ND*','',x)
x = re.sub(r'[0-9]RD*','',x)
x = x.split()
tlen = len(x)
if tlen == 1:
    bookkey += x[0][0:8]
if tlen == 2:
    bookkey += x[0][0:4]
    bookkey += x[1][0:4]
if tlen > 2 and tlen < 7:
    for y in x:
        bookkey += y[0]
if tlen >7:
    for y in range(7):
        bookkey += x[y][0]
    bookkey += 'Itd'    
print(bookkey)
