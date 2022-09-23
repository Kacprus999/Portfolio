import numpy as np
import numpy.random as random

tab1 = np.random.randint(-100,101, (9,9))
print(tab1)

tab1 = tab1[tab1%2==0]
print(tab1)

print(np.sort(tab1))