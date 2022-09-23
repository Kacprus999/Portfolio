from xmlrpc.client import INVALID_XMLRPC
import numpy as np
import matplotlib.pylab as plt
from scipy import misc
from scipy.stats import norm

#normal
Sx = 1.0 * np.random.randn(1000) + 1.0
Sy = 1.0 * np.random.randn(1000) + 1.0
data = [Sx,Sy]
plt.scatter(Sx,Sy)

#streched
Sx_wide = Sx*3
data_wide = [Sx_wide,Sy]
#plt.scatter(data_wide[0],data_wide[1])

#rotated
theta = np.radians(45)
r = np.array(( (np.cos(theta), -np.sin(theta)),
               (np.sin(theta),  np.cos(theta)) ))
rotated = np.matmul(r,data)

x_rot = Sx*np.cos(theta) + Sy*np.sin(-1*theta)
y_rot = Sx*(np.sin(theta)) + Sy*np.cos(theta)

#plt.scatter(rotated[0],rotated[1])
#plt.scatter(x_rot,y_rot)

#rotated and streched
rotated_wide = np.matmul(r,data_wide)
x_rot_wide = x_rot*3
#plt.scatter(rotated_wide[0],rotated_wide[1])
#plt.scatter(x_rot_wide,y_rot)



#coeficient 
coef = np.corrcoef(data)
coeft = np.corrcoef(rotated_wide)
coeft1 = np.corrcoef(x_rot_wide,y_rot)

# print(coef,"\n\n",coefr,"\n\n",coeft)
# print("\n\n\n")

#covariance matrix
cov = np.cov(data)
covt = np.cov(rotated_wide)
covt1 = np.cov(x_rot_wide,y_rot)
print(covt)

#eigendecomposition
eig = np.linalg.eig(cov)
eigt = np.linalg.eig(covt)
eigt1 = np.linalg.eig(covt1)

w, v = np.linalg.eig(covt)
w1, v1 = np.linalg.eig(covt1)

# print(eig,"\n\n",eigr,"\n\n",eigt)
print(w)
print(v)

#diag_vec = np.diag(v)
# diag_vec1 = np.diag(v1)
# print(diag_vec)

#inverse
inverse = np.matmul(np.sqrt(w),v)
inverse1 = np.matmul(np.sqrt(w1),v1)
print(inverse)
# print(inverse1)

# inv = np.sqrt(w) @ diag_vec
# inv1 = np.matmul(np.sqrt(w1),diag_vec)

inversed = np.matmul(inverse,data)
inversed1 = np.matmul(inverse1,data)


# inv_x = Sx*inverse[0]
# inv_y = Sy*inverse[1]
# plt.scatter(inv_x,inv_y)

#plt.scatter(inversed,Sy)
plt.scatter(inversed1,Sy)

plt.show()