import numpy as np
import sys

# nalezy wprowadzic macierz oraz wektor jako dodatkowa kolumne macierzy
a = [
    [6,-2,2,-4,0],
    [12,-2,3,10,22],
    [3,2,8,-6,19],
    [-6,4,6,-18,0]
]
n = len(a)

# wlasciwy algorytm
for i in range(n):

    print('------ step ' + str(i+1) + ' -----')
    print('macierz wejsciowa')
    y = np.array(a)
    print(y)
    
    #czesciowy wybor elementu glownego
    max = abs(a[i][i])
    max_pos = i
    for j in range(i+1, n):
        if abs(a[j][i]) > max:
            max = a[j][i]
            max_pos = j
    if(max_pos != i):
        a[i], a[max_pos] = a[max_pos], a[i]
        print('(' + str(i) +') po zmianie elementu glownego (zmiana ' + str(i) + ' wiersza na ' + str(max_pos))
        y = np.array(a)
        print(y)
    else:  
        print('(' + str(i) +') nie ma potrzeby zmiany elementu glownego')

    if a[i][i] == 0.0:
        sys.exit('(' + str(i) +') dzielenie przez zero')

    #eliminacja gaussa
    print('(' + str(i) +') eliminacja gaussa')
    print('element glowny: ' + str(a[i][i]))
    for j in range(i+1, n):
        mnoznik = a[j][i]/a[i][i]
        print('mnoznik dla wiersza ' + str(j+1) + ' = ' + str(mnoznik))
        
        for k in range(n+1):
            a[j][k] = a[j][k] - mnoznik * a[i][k]

    print('(' + str(i) +') po eliminacji gaussa')
    y = np.array(a)
    print(y)

#tablica wynikowa
x = np.zeros(n)

#obliczenie przeszukiwaniem wstecz (back substitution)
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    x[i] = x[i]/a[i][i]

#wynik
for i in range(n):
    print('X%d = %0.2f' %(i+1,x[i]), end = '\t')