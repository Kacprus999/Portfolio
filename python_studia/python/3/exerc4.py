import numpy as np
import numpy.random as random
from numpy.ma import masked_array
import matplotlib.pylab as plt
import matplotlib.cm as cm


tab = np.random.uniform(-8.0,8.0,size=(500,2))
print(tab)
x,y = tab[:,0],tab[:,1]
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)

ta = t[t<3.14]
tb = masked_array(t,t>=180)
print(ta)
fig = plt.figure()
ax = fig.add_subplot(projection='polar')

colors = cm.get_cmap(name='jet')
ca = ax.scatter(r,ta,c=ta,cmap='jet')
#cb = ax.scatter(r,tb)

plt.show()