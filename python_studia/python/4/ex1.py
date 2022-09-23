import numpy as np
import matplotlib.pylab as plt
import scipy
from scipy.linalg import lu

a = np.array([[2,3],[5,4]])
b = np.array([4,23])

x1 = np.array(range(10))
y1 = (4-2*x1)/3
x2 = np.array(range(10))
y2 = (23-5*x2)/4


print(lu(a))

rank = np.linalg.matrix_rank(a)
cond = np.linalg.cond(a)

x=np.linalg.solve(a,b)

print(rank)
print(cond)

print(x)
plt.plot(x1,y1,'b')
plt.plot(x2,y2,'r')
plt.show()

