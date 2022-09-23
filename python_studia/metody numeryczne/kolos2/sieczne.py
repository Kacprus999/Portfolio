#sieczne
import math

def fun(x):
    return x * x * x - x * x - 2

def sieczne(x1, x2):
    n = 0
    xm = 0
    x0 = 0
    c = 0
    iter = 0
    
    if fun(x1) * fun(x2) < 0:
        while True:
            iter = iter + 1
            x0 = ((x1 * fun(x2) - x2 * fun(x1)) / (fun(x2) - fun(x1)))
            c = fun(x1) * fun(x0)
            x1 = x2
            x2 = x0
            n = n + 1
            if c == 0:
                break
            xm = ((x1 * fun(x2) - x2 * fun(x1)) / (fun(x2) - fun(x1)))
            if abs(xm - x0) < epsilon and fun(x0) < epsilon:
                break
        return x0,iter

x1 = 1
x2 = 2
epsilon = 0.00001
wynik, iter = sieczne(x1, x2)

#miejsca po przecinku
print("%.10f" % wynik)
print("iteracje: " + str(iter))
