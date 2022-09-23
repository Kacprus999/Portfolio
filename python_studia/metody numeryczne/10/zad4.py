import numpy as np


d1 = np.zeros((5,5))
d2 = np.array([0.01])

x = np.arange((5,5), dtype=np.double)

d1 = np.diag(np.diag(d2))
print(d1)

