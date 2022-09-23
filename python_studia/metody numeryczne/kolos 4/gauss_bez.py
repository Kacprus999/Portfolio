import numpy as np
import sys
from mpmath import *

mp.dps = 500
# nalezy wprowadzic macierz oraz wektor jako dodatkowa kolumne macierzy
a = [
    [-10**(-30),1,1],
    [1,1,2]
]
n = len(a)

# wlasciwy algorytm
for i in range(n):

    print('------ step ' + str(i+1) + ' -----')
    print('macierz wejsciowa')
    y = np.array(a)
    print(y)

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