# styczne bez stopnia i z

def fun(x):
    return x**3 -7
def poch(x):
    return 3*x**2

def newton_styczne(x):
    # poczatkowa liczba iteracji
    iter = 0
    while True:
        iter = iter + 1
        h = x
        x = x - fun(x) / poch(x)
        print(x)
        if abs(h - x) < eps and fun(x) < eps:
            return x,iter

def newtonStyczne_n(x):
    iter = 0
    # stopien pierwiastka
    n = 2
    while True:
        iter = iter + 1
        h = x
        x = x - n * (fun(x) / poch(x))
        if abs(h - x) < eps and fun(x) < eps:
            return x,iter

#dokladnosc
eps = 10**(-10)
x0 = 1

wynik, iter = newton_styczne(x0)
# w przypadku stopnia pierwiastka
# wynik, iter = newtonStyczne_n(x0)

# ilosc miejsc po przecinku
print("%.3f" % wynik)
print("iteracje: " + str(iter))
