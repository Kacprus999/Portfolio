# program do tworzenia funkcji sklejanej na podstawie podanych danych
# mam nadzieję, że będzie działac poprawnie

# uzupełnij tabelę punktami x (albo t) i punktami y

t = [0,1,4,5]
y = [26,7,25,4]

n = len(t) - 1
# konstruujesz n wielomianów S_i(x) dla i = 0,1,2...n-1
print("Należy skonstruować " + str(n) + " wielomianów")

h = []
b = []
for i in range(n):
    h_i = t[i + 1] - t[i]
    h.append(h_i)
    b_i = (6 * (y[i + 1] - y[i])/ h[i])
    b.append(b_i)

print("h: ", h)
print("b: ", b)

u = []
v = []

u_1 = 2 * (h[0] + h[1])
u.append(u_1)
v_1 = b[1] - b[0]
v.append(v_1)

for i in range(2, n):
    u_i = 2 * (h[i] + h[i - 1]) - (h[i - 1]) ** 2 / u[i - 2]
    u.append(u_i)
    v_i = (b[i] - b[i - 1]) - (h[i - 1] * v[i - 2] / u[i - 2])
    v.append(v_i)

print("u: ", u)
print("v: ", v)

#z jest odwrócone i tutaj zaczyna się problem (jak chcesz to rozkminić to proszę bardzo ale nie polecam w luj)
z = []
for n in range(n+1):
    z.append(0)

print("z pierwsze: ", z)
reversed_range = range(n-1, 0, -1)

for i in reversed_range:
    z_i = (v[i-1] - h[i] * (z[i-n])) / u[i-1]
    z.pop(i)
    z.insert(i, z_i)
    print("z: ", z)

print("z ost: ", z)

#Si(x) = yi +(x-ti)(Bi + (x-ti)(zi/2+1/6hi(x-ti)(zi+1-zi)))
#Bi = -hi/6*zi+1 -hi/3 *zi + 1/hi*(yi+1-zi)