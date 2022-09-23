import numpy as np


def zeros_matrix(n):
    M=[]
    while len(M) < n:
        M.append([])
        while len(M[-1]) < n:
            M[-1].append(0.0)
    return M

def matrix_multiply(A, B):

    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    # Section 2: Store matrix multiplication in a new matrix
    C = zeros_matrix(rowsA)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def get_b(i, pos):
    if pos == i:
        return 1
    else:
        return 0

def get_sum(x_array, wiersz, j, k):
    sum = 0
    for i in range(j, k):
        sum = sum + (x_array[i] * wiersz[i])
    return sum
            

def substitution (macierz, i):
    x_array = [0 for i in range(i)]
    for j in range(i, len(macierz)):
        b = get_b(j, i)
        sum = get_sum(x_array, macierz[j], i, j)
        x = float(float(b) - float(sum))/float(macierz[j][j])
        x_array.append(x)
    return x_array
        
# dziala na dolne
def odwrotnosc (macierz):
    macierz_length = len(macierz)
    wynik = [[0 for i in range(macierz_length)] for j in range(macierz_length)]
    for i in range(0, macierz_length):
        subs = substitution(macierz, i)
        for j in range(0, macierz_length):
            wynik[j][i] = subs[j]
    return wynik

def upper_to_lower_triangular (macierz):
    macierz_length = len(macierz)
    wynik = [[0 for i in range(macierz_length)] for j in range(macierz_length)]
    for i in range(0, macierz_length):
        for j in range(0, macierz_length):
            wynik[i][j] = macierz[macierz_length-i-1][macierz_length-j-1]
    return wynik

def inverse_lower (macierz):
    return odwrotnosc(macierz)

def inverse_upper (macierz):
    temp = upper_to_lower_triangular(macierz)
    temp = odwrotnosc(temp)
    return upper_to_lower_triangular(temp)


n = 3 # stopien macierzy

A = [[5, 3, 2], 
     [1, 2, 0], 
     [3, 0, 4] ] # macierz do obliczenia / macierz wejsciowa

# tworznie "pustych" macierzy L i U / jako 0
L = zeros_matrix(n)
U =zeros_matrix(n)

inv_L = zeros_matrix(n)      
inv_U = zeros_matrix(n)



det = 1 # wyznacznik

for i in range(n):

    # gorny U
    for j in range(i,n):

        # sumowanie L(i,j) * U(j,k)
        sum = 0
        for k in range(i):
            sum += (L[i][k] * U[k][j])

        U[i][j] = A[i][j] - sum
        if (i==j):
            det *= U[i][i]
        
    # dolny L
    for j in range(i,n):
        if (i==j):
            L[i][i] = 1 # tworzenie identycznosciowej / przekatna na 1
        else:

            # sumowanie L(k,j) * U(j,i)
            sum = 0
            for k in range(i):
                sum += (L[j][k]*U[k][i])
            
            L[j][i] = float( (A[j][i]-sum) / U[i][i])

if det == 0:
    print("macierz osobliwa")
else:
    # for i in range(n): #kolumna
    #     for j in range(i,n): #wiersz
    #         if(i==j):
    #             inv_L[i][i] = 1/L[i][i]
    #             inv_U[i][i] = 1/U[i][i]
    #         else:
    #             sum = 0
    #             inv_L[j][i] = - L[j][i]/(L[j-1][i]*L[j][i+1])

    #             # inv_U[i][j] = -U[i][j]/(U[i-1][j]*U[j][i+1])
    inv_L = inverse_lower(L)
    inv_U = inverse_upper(U)
    inv_A = matrix_multiply(inv_U, inv_L)

# A = np.array(A)
L = np.array(L)
U = np.array(U)
inv_L = np.array(inv_L)
inv_U = np.array(inv_U)
inv_A = np.array(inv_A)


# print("A: ",A)
print("L: \n",L)
print("inverse L: \n",inv_L)

print("U: \n",U)
print("inverse U: \n",inv_U)
print("det: ",det)

print("inverse A: \n",inv_A)