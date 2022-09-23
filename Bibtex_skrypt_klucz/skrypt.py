import re


rx_dict = {
    'rekord': re.compile(r'(@.*)'),
    'authorbook': re.compile(r'Book-Author = \{[a-zA-Z0-9_\-,\.\'\\ ]*\},\n'),
    'authorgroupbook': re.compile(r'Book-Group-Author = \{[a-zA-Z0-9_\-,\.\'\\ ]*\},\n'),
    'author': re.compile(r'Author = \{[a-zA-Z0-9_\-,\.\'\\ ]*\},\n'),
    'author-potrojny':re.compile(r'   [a-zA-Z0-9_\-,\.\'\\ \n]*\n'),
    'author-podwojny':re.compile(r'Author = \{[a-zA-Z0-9_\-,\.\'\\ ]*\n'),
    'journal': re.compile(r'Journal = \{\{[a-zA-Z0-9_\-,\.\'\\ \n&\&]*\}\},\n'),
    'journal-podwojny':re.compile(r'Journal = \{\{[a-zA-Z0-9_\-,\.\'\\ \n]*'),
    'book': re.compile(r'Booktitle = \{\{[a-zA-Z0-9_\-,\.\'\\ \n]*\}\},\n'),
    'book-potrojny':re.compile(r'   [a-zA-Z0-9_\-,\.\'\\ \n]*\n'),
    'book-podwojny':re.compile(r'Booktitle = \{\{[a-zA-Z0-9_\-,\.\'\\ \n]*'),
    'year': re.compile(r'Year = \{\{[0-9][0-9][0-9][0-9]\}\}'),
    'article-number': re.compile(r'Article-Number = \{\{'),
    'ead': re.compile(r'Early Access Date = \{\{[a-zA-Z0-9 ]*\}\}'),
    'pages': re.compile(r'Pages = \{\{[0-9\-&\\]*\}\}'),
    'threespaces': re.compile(r'   '),
    'Title':re.compile(r'Title = '),
    #'space': re.compile(r' '),
    #'basickey': re.compile(r'WOS:[0-9]{1,20}'),
}

def stripper(sample, line):
    if sample == 'rekord':
       x = line.split(" ")
       return x[0]
    if sample == 'author':
        iloscand = line.count(' and ')
        authkey=''
        if line.count('Author') == 0:
            return authkey
        x = line.split("Author = {")
        x = x[1].split(' and ')

        for i in range(min(3, iloscand+1)):
            surname = x[i].split(',')[0].strip()
            y = surname.find("'")
            if y > -1:
                authkey += surname[y+1:y+4].strip()
            else:
                authkey += surname[0:3].strip()
        if iloscand > 2:
            authkey += 'ETAL'
        return authkey
    if sample == 'year':
        yearkey=''
        x = line.split("Year = {{")
        x = x[1].split('}},\n')
        yearkey += x[0]
        return yearkey
    if sample == 'journal':
        jourkey=''
        x = line.split("Journal = {{")
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
        x = x.replace(':', '')
        x = x.split()

        tlen = len(x)
        if tlen == 1:
            jourkey += x[0][0:8]
        if tlen == 2:
            jourkey += x[0][0:4]
            jourkey += x[1][0:4]
        if tlen > 2:
            for y in x:
                jourkey += y[0]
        return jourkey
    if sample == 'book':
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
        x = x.replace(':', '')
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
        return bookkey
    if sample == 'article-number':
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
        return artkey
    if sample == 'ead':
        eadkey=''
        x = line.split("Early Access Date = {{")
        x = x[1].split('}},\n')
        x = x[0].split()
        eadkey += x[1]
        return eadkey
    if sample == 'pages':
        pgkey=''
        x = line.split("Pages = {{")
        x = x[1].split('}},\n')
        x = x[0].split('-')
        pgkey += x[0]
        return pgkey
     
    return None


def parse_line(line):
    #przeszukuje linie w poszukiwaniu trafien do rx_dict
    #zwraca klucz i wynik pierwszego trafienia
    for key, rx in rx_dict.items():
        match =rx.search(line)
        if match:
            return key
    #jesli nie ma zadnych trafien
    return None
    
def parse_file(filepath):
    print('zaczynam parsowac plik')
    newkey = ''
    index=0
    zawartosc = []
    prevreg = ''
    prevline = ''
    tempkey = ''
    wasbook = False
    isbook = False
    isproc=False
    isauthor = False
    wasauthor = False
    isnotauthor=False
    #otwarcie i czytanie pliku linia po lini
    with open(filepath, 'r', encoding="utf8") as file_object:
        
   
        for line in file_object:
            #pobieranie kolejnej lini tekstu
            #line = file_object.readline()
            
            #zapisywanie rekordu linia po lini do tabeli
            zawartosc.append(line)
            
            #sprawdzenie trafienia
            key = parse_line(line)         
            
            if key == 'rekord':
                poczatek = index
                newkey += stripper('rekord', line)
                if newkey == '@incollection{':
                    isbook=True
                if newkey == '@inproceedings{':
                    isproc=True
            if key == 'authorbook' or 'authorgroupbook':
                isnotauthor=True
            if key == 'author':
                newkey += stripper('author', line)
            if (key=='author-podwojny'):
                prevline += line
                prevreg=key
            if (key=='author-potrojny'):
                prevreg=''
                prevline += line
                prevreg=key
                isauthor=True
            if key == 'title':
                prevreg=''
                wasauthor=True
                isauthor=False
            if (prevreg=='author-podwojny' and key == 'threespaces'):
                newline = prevline+line
                newkey += stripper('author', newline)
                prevreg=''
                newline=''
                prevline=''
            if (prevreg=='author-potrojny' and key == 'threespaces' and isauthor==True and wasauthor==False):
                newline = prevline+line
                newkey += stripper('author', newline)
                prevreg=''
                newline=''
                prevline=''
                wasauthor=True
            if key == 'journal':
                tempkey += stripper('journal', line)
            if (key=='journal-podwojny'):
                prevline = line
                prevreg=key
            if (prevreg=='journal-podwojny' and key == 'threespaces'):
                newline = prevline+line
                tempkey += stripper('journal', newline)
                prevreg=''
                newline=''
                prevline=''
            if key == 'book':
                if isbook==True:
                    tempkey+='Book'
                if isproc==True:
                    tempkey+='InProc'
                tempkey += stripper('book', line)
            if (key=='book-podwojny'):
                prevline += line
                prevreg=key
            if (key=='book-potrojny'):
                prevreg=''
                prevline += line
                prevreg=key
            if (prevreg=='book-podwojny' and key == 'threespaces' and (isbook==True or isproc==True)):
                newline = prevline+line
                if isbook==True:
                    tempkey+='Book'
                if isproc==True:
                    tempkey+='InProc'
                tempkey += stripper('book', newline)
                prevreg=''
                newline=''
                prevline=''
            if (prevreg=='book-potrojny' and key == 'threespaces' and wasbook==False and (isbook==True or isproc==True)):
                newline = prevline+line
                if isbook==True:
                    tempkey+='Book'
                if isproc==True:
                    tempkey+='InProc'
                tempkey += stripper('book', newline)
                prevreg=''
                newline=''
                prevline=''
                wasbook=True
            if key == 'year':
                newkey += stripper('year', line)
                newkey += tempkey
            if key == 'article-number':
                newkey+='a'
                newkey += stripper('article-number', line)
            if key == 'ead':
                newkey += stripper('ead', line)
                newkey += tempkey
            if key == 'pages':
                newkey+='p'
                newkey += stripper('pages', line)            
            if line == '\n':
                newkey += ',\n'
                zawartosc[poczatek-1] = newkey
                i=0
                newfile = open('1-4920noweklucze.bib', 'a', encoding="utf8")
                for x in zawartosc:
                    newfile.write(x)
                index=0
                print(newkey)
                wasauthor=False
                wasbook=False
                isbook=False
                isproc=False
                isauthor = False
                isnotauthor=False
                newkey=''
                tempkey=''
                newfile.close()
                zawartosc=[]
                
            index += 1

    return None
filepath = '1-4920test.bib'
parse_file(filepath)
print('Koniec pracy')
