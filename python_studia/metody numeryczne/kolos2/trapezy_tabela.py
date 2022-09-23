#metoda trapezow tabela

def trapezy(x,fx):
    a = x[0]
    b = x[-1]
    n = len(x)-1

    h = (b - a)/n
    Qf = h/2 * (fx[0] + 2*(sum(fx[1:-1])) + fx[-1])
    
    return Qf

#tabela
x = [-2, -1, 0, 1, 2]
fx = [0, 2.75, 4, 6.75, 8]

wynik = trapezy(x,fx)


# ilosc miejsc po przecinku
print("%0.5f" % wynik)

