# program do bisekcji
import math

def fun(x):
    return x * x * x - x * x - 2

def bisekcja(a, b):
    iter = 0
    c = (a + b) / 2

    while True:
        c = (a + b) / 2
        print(c)
        iter = iter + 1
        if fun(c) == 0 or abs(fun(c)) < epsilon:
            break
        y = fun(a) * fun(c)
        if y < 0:
            b = c
        else:
            a = c

    return c, iter


# calka gorna i dolna oraz epsilon maszynowy
a = 1
b = 2
epsilon = 0.00001
wynik, iter = bisekcja(a, b)

#liczba miejsc po przecinku
print("%.10f" % wynik)
print("iteracje" + str(iter))