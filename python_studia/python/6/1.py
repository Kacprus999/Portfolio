import numpy as np
import matplotlib.pylab as plt
from scipy import misc
from matplotlib.image import NonUniformImage
from scipy.stats import norm

x = np.load('daneX.npy')
y = np.load('daneY.npy')

H, xedges, yedges= np.histogram2d(x,y)
# H=H.T

fig = plt.figure()
ax = fig.add_subplot(121)
plt.imshow(H)
plt.colorbar()

ax = fig.add_subplot(122, aspect='equal')
plt.contourf(H)
plt.colorbar()

plt.show()