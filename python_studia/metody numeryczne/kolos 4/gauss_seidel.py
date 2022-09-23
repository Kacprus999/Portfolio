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


def checkDiagonallyDominant(m, n):
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum = sum + abs(m[i][j])
        sum = sum - abs(m[i][i])
        if abs(m[i][i]) < sum:
            return False
    return True


matrix2 = [[4.0, -1.0, 1], [2.0, 5.0, 2.0], [1.0, 2.0, 4.0]]
vector2 = [8.0, 3.0, 11.0]
guess = [1.0, 1.0, 1.0]
n = 3

matrix3 = [[4.0, -1.0, -1.0, 0.0], [-1.0, 4.0, 0.0, -1.0], [-1.0, 0.0, 4.0, -1.0], [0.0, -1.0, -1.0, 4.0]]
vector3 = [1.0, 2.0, 0.0, 1.0]
guess3 = [1.0, 1.0, 1.0, 1.0]

matrix4 = [[1.0, 1.0, 1.0], [1.0, 2.0, 4.0], [1.0, 3.0, 9.0]]
vector4 = [3.0, 7.0, 13.0]

matrix5 = [[1.0, 2.0, -2.0], [1.0, 1.0, 1.0], [2.0, 2.0, 1.0]]
vector5 = [2.0, 4.0, 7.0]

eps = 0.0000000001


def checkSeidel(matrix, vector, guess, n, eps):
    if checkDiagonallyDominant(matrix, n):
        print("Yes")
        SeidelMatrix(matrix, vector, guess, n, eps)
    else:
        print("No")


checkSeidel(matrix2, vector2, guess, n, eps)