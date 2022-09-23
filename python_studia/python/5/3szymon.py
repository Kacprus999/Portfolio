import numpy as np
import matplotlib.pylab as plt
from scipy import misc
from scipy.stats import norm

samp1 = norm.rvs(size=1000, loc=1.0, scale=1.0)
samp2 = norm.rvs(size=1000, loc=1.0, scale=1.0)
samp3 = samp1 *3
plt.scatter(samp1, samp2)
plt.scatter(samp3, samp2)

data = [samp3, samp2]
rotation_matrix = [
    [np.cos(np.deg2rad(45)), -np.sin(np.deg2rad(45))],
    [np.sin(np.deg2rad(45)), np.cos(np.deg2rad(45))]
]
result = np.matmul(rotation_matrix, data)
plt.scatter(result[0], result[1])
plt.show()