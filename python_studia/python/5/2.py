import numpy as np
import matplotlib.pylab as plt
from scipy import misc
from scipy.stats import norm

mu = np.zeros(100)
for i in range(100):
    data = np.random.normal(3.0,1.0,100)
    mu[i] = np.mean(data)

std = np.std(mu)
print(std)

mu1 = np.zeros(1000)
for i in range(1000):
    data = np.random.normal(3.0,1.0,1000)
    mu1[i] = np.mean(data)

std1 = np.std(mu1)
print(std1)

#plt.hist(mu)
#plt.hist(mu1,alpha=0.5)
plt.show()