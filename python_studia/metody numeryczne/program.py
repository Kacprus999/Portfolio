import numpy as np
from sympy import Symbol, Eq

t=[0,1,2,3,4] 
y=[0,0,0,1,0] 
h=[]
b=[]
u=[0,0]
v=[0,0]
z=[]
B=[]
a = Symbol('x')
n=len(t)

for x in range(n):
    z.append(0)

print(z)

for x in range(n-1):
    h.append(t[x+1]-t[x])
    b.append(6(y[x+1]-y[x])/h[x])

u[1]=2(h[0]+h[1])
v[1]=b[1]-b[0]

for x in range(2, n-1):
    u.append(2(h[x]+h[x-1])-((h[x-1]**2)/u[x-1]))
    v.append((b[x]-b[x-1])-((h[x-1]*v[x-1])/u[x-1]))

print(u)
print(v)

for x in range(n-2, 0, -1):
    z[x]=((v[x]-h[x]*z[x+1])/u[x])

print(z)
print(" ")

for x in range(n-1):
    B=(0-(h[x]/6)*z[x+1])-((h[x]/3)*z[x])+((1/h[x])*y[x+1]-y[x])
    S=y[x]+(a-t[x])(B+(a-t[x])((z[x]/2)+((1/(6*h[x]))(a-t[x])*(z[x+1]-z[x]))))
    print("B")
    print(B)
    print(" ")
    print("S")
    print(S)
    print(" ")