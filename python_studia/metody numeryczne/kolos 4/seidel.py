# metoda seidela
def SeidelMatrix(A, b, x, N, eps):
    iterationNumber = 10000
    xPrevious = [0.0 for i in range(N)]
    for i in range(iterationNumber):
        for j in range(N):
            xPrevious[j] = x[j]
        for j in range(N):
            summ = 0.0
            for k in range(N):
                if k != j:
                    summ = summ + A[j][k] * x[k]
            x[j] = (b[j] - summ) / A[j][j]
        differenceNorm = 0.0
        oldNorm = 0.0
        for j in range(N):
            differenceNorm = differenceNorm + abs(x[j] - xPrevious[j])
            oldNorm = oldNorm + abs(xPrevious[j])
        if oldNorm == 0.0:
            oldNorm = 1.0
        norm = differenceNorm / oldNorm
        if (norm < eps) and i != 0:
            print("Ostateczny wektor wynosi [", end="")
            for j in range(N - 1):
                print(x[j], ",", end="")
            print(x[N - 1], "]. Liczba iteracji", i + 1)
            return
    print("Brak rozwiązania dla tej macierzy")


# sprawdzam czy macierz mozna uzyc do metody seidela
def checkDiagonallyDominant(m, n):
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum = sum + abs(m[i][j])
        sum = sum - abs(m[i][i])
        if abs(m[i][i]) < sum:
            return False
    return True


matrix2 = [[1, 2, -2], 
            [1, 1, 1], 
            [2, 2, 1]]
vector2 = [2.0, 3.0, -4.0]
guess = [0.0, 0.0, 0.0]
n = 3

eps = 10**(-10)


def checkSeidel(matrix2, vector2, guess2, n, eps):
    if checkDiagonallyDominant(matrix2, n):
        print("Yes")
        SeidelMatrix(matrix2, vector2, guess, n, eps)
    else:
        print("No")


checkSeidel(matrix2, vector2, guess, n, eps)
