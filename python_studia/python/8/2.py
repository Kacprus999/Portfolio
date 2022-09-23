import numpy as np
import matplotlib.pyplot as plt


def ode_FE(dt, T):
    steps = int(round(float(T)/dt))
    s = np.zeros(steps + 1)
    i = np.zeros(steps + 1)
    r = np.zeros(steps + 1)

    t = np.linspace(0, steps * dt, len(s))

    s[0] = 1000
    i[0] = 1
    r[0] = 0

    for n in range(steps):
        s[n+1] = s[n] + dt*ds(i[n],s[n])
        i[n+1] = i[n] + dt*di(i[n],s[n])
        r[n+1] = r[n] + dt*dr(i[n])

    return s, i,r, t


S = 1000
I = 1
R = 0

beta = 0.5
gamma = 0.1
t = 200
N = S + I + R

#f1 = -((beta*I*S)/N)*0.1
def ds(i,s):
    return -((beta*i*s)/N)

#f2 = (((beta*I*S)/N) - gamma*I) * 0.1
def di(i,s):
    return (((beta*i*s)/N) - gamma*i)

#f3 = (gamma * I) * 0.1
def dr(i):
    return (gamma * i)



s1,i1,r1,t1 = ode_FE(0.1,200)

#fig,axs = plt.subplots(3)
#axs[0].plot(t1,s1)
#axs[1].plot(t1,i1)
#axs[2].plot(t1,r1)

plt.figure()
plt.plot(t1, s1)
plt.plot(t1, i1)
plt.plot(t1, r1)


plt.show()