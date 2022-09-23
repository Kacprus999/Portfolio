import numpy as np


st = 10

A = np.array([[1,3,4],[2,5,6],[7,8,9]]) #macierz wyjsciowa

if np.linalg.det(A) == 0:
    print("Macierz jest osobliwa wiec nie mozna wyznaczyc odwrotnosci")


X = np.zeros((st,st)) # macierz odwrotna
I = np.identity(st) #macierz idenentycznosciowa




print(A)