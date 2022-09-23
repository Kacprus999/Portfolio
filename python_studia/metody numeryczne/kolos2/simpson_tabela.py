#simpson lub parabole zaawnsowany na tabeli

def simpson(x,fx):
    a = x[0]
    b = x[-1]
    n = len(x)

    h = (b - a)/(n-1)
    Qf = (h/3) * (fx[0] + 4*sum(fx[1:n-1:2]) + 2*sum(fx[2:n-2:2]) + fx[-1])
    
    return Qf

#przepisanie tabeli
x = [1, 1.5, 2, 2.5, 3]
fx = [2, 5.75, 11, 17.75, 26]

wynik = simpson(x,fx)


# ilosc miejsc po przecinku
print("%0.5f" % wynik)
