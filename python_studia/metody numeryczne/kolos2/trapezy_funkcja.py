#metody trapezow (funkcje liniowe) funkcja
import math

def fun(x):
    wzor_funkcji = math.exp()**x - math.sin(x)
    return wzor_funkcji

def trapezy(x0, xn, n):

    h = (xn - x0)/n
    wynik = fun(x0) + fun(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        wynik = wynik + 2 * fun(k)

    wynik = wynik * h/2
    return wynik

#calka gorna i dolna oraz rzad
a = -4
b = -3
n = 4

wynik = trapezy(a, b, n)

#ilosc miejsc po przecinku
print("%0.6f " % wynik)
