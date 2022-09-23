import numpy as np
import matplotlib.pylab as plt

time = np.linspace(0, 500, 501)
k = np.log(1015)/240

p = 10*np.exp(1)**(k*time)

# p = np.linspace(10,100000,1)

X = np.linspace(0, 500, 500)
Y = np.linspace(10, 50000, 500)
X, Y = np.meshgrid(X, Y)

dxdt = k*Y
dt = np.ones(X.shape)
dx = dxdt * dt


plt.figure()
plt.streamplot(X, Y, dt, dx)

#plt.plot(time, p)
plt.show()


# t=0 x=10      10=C
# t=240h x=1015 1015=e^240K
# K = ln1015/240
# P(t) = e^Kt

# t=480h x=?
# 