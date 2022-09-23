from cmath import sqrt
import numpy as np
from mpmath import *

mp.dps = 10

def zeros_matrix(rows, cols):
    M=[]
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M

def matrix_multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    C = zeros_matrix(rowsA,colsB)

    if colsA != rowsB:
        raise ArithmeticError("liczba kolumn pierwszej macierzy musi być równa ilości wierszy drugiej")

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def matrix_addition(A,B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] + B[i][j]

    return C

def matrix_subtraction(A,B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]

    return C

def LDU(A):   
    L = zeros_matrix(n,n)
    D = zeros_matrix(n,n)
    U = zeros_matrix(n,n)
    inv_d = zeros_matrix(n,n)
    min_inv_d = zeros_matrix(n,n)

    for i in range(n):
        for j in range(n):
            if(i==j):
                D[i][i] = A[i][i]
                inv_d[i][i] = 1/A[i][i]
                min_inv_d[i][i] = - inv_d[i][i]
            elif(j>i):
                U[i][j] = A[i][j]
            else:
                L[i][j] = A[i][j]
    return L,D,U,inv_d,min_inv_d

def Jacobi(A,eps,lu,inv_d,min_inv_d,b,x):
    
    wek_res = matrix_multiply(A,x)
    wek_res = matrix_subtraction(b,wek_res)
    wek_res = abs(mp.sqrt( mp.root(wek_res[0][0],2) + mp.root(wek_res[1][0],2) + mp.root(wek_res[2][0],2)))
    # wek_res2 = abs(sqrt(pow(wek_res[0][0],2) + pow(wek_res[1][0],2) + pow(wek_res[2][0],2)))
    iter = 0

    while(wek_res > eps ) :
        x = matrix_multiply(lu,x)
        x = matrix_multiply(min_inv_d,x)
        x = matrix_addition(x,matrix_multiply(inv_d,b))
        iter += 1
        wek_res = matrix_multiply(A,x)
        wek_res = matrix_subtraction(b,wek_res)
        wek_res = abs(mp.sqrt( mp.root(wek_res[0][0],2) + mp.root(wek_res[1][0],2) + mp.root(wek_res[2][0],2)))

    return x,iter


eps = 10**(-10)  # epsilon; dokladnosc


iter = 0    # liczba iteracji
A = [[1, 2, -2], 
     [1, 1, 1], 
     [2, 2, 1]]  # macierz do obliczenia / macierz wejsciowa
n = len(A) # stopien macierzy

b = [[2],
    [3],
    [-4]]

x = [[0],
    [0],
    [0]]

L,D,U,inv_d,min_inv_d = LDU(A)
lu = matrix_addition(L,U)

A = np.array(A)
L = np.array(L)
D = np.array(D)
U = np.array(U)
inv_d = np.array(inv_d)

# print("A: \n",A)
# print("L: \n",L)
# print("D: \n",D)
# print("U: \n",U)
# print("inv_d: \n",inv_d)


wynik,iter = Jacobi(A,eps, lu, inv_d, min_inv_d,b,x)
wynik = np.array(wynik)

print("wynik: \n",wynik)
print("liczba iteracji: ",iter)