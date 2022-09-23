import math

#funkcja
def fun(x):
    return x * x * x + 1

def simp(x0, xn, n):
    h = (xn - x0)/n

    wynik = fun(x0) + fun(xn)

    for i in range(1, n):
        k = x0 + i * h
        if i % 2 == 0:
            wynik = wynik + 2 * fun(k)
        else:
            wynik = wynik + 4 * fun(k)

    wynik = wynik*h/3
    return wynik

a = 1
b = 2
n = 3

wynik = simp(a,b,n)
#liczba miejsc po przecinku
print("%0.6f" % wynik)