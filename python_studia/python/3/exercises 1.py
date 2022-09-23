import numpy as np
import numpy.random as random

tab1 = np.random.randint(0,high=101,size=25)
print(tab1)

tab1[tab1<50]=0
print(tab1)

tab1[np.argmax(tab1)] = 200
print(tab1)