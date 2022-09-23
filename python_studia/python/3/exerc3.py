import numpy as np
import numpy.random as random
import matplotlib.pylab as plt

x = np.arange(0,3*np.pi,0.01)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('center')

idx = np.argwhere(np.abs(y-z) < 0.1)


plt.plot(x[idx],y[idx],'ro',x[idx],z[idx], 'ro')
plt.show()
