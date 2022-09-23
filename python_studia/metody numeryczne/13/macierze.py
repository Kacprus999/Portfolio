
macierz = [
    [1,0,0],
    [2,3,0],
    [4,5,6]
]

macierz2 = [
    [6,5,4],
    [0,3,2],
    [0,0,1]
]

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

result = inverse_upper(macierz2)
for i in range(0, 3):
    print(result[i])


