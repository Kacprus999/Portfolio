
from numpy import matrix as mtx, identity as I
import numpy as np
from numpy import set_printoptions, tril, triu
set_printoptions(precision=5, suppress=True)

def triangular_inversion(triang_arg):
    """Counts inversion of a triangular matrix (lower or upper).

    Args:
        triang_arg (np.matrix, np.array): triangular matrix for inversion

    Returns:
        np.matrix: inverse of triangular matrix
        
    Raises:
        Exception: An error occured while passing non-square matrix
        Exception: An error occured while passing non-triangular matrix
        Exception: An error occured while passing singular matrix

    """
    if len(triang.shape) != 2 or triang_arg.shape[0] != triang_arg.shape[1]:
        raise Exception('Matrix is non-square')
    if triang_arg not in [tril(triang_arg), triu(triang_arg)]:
        raise Exception('Matrix is not triangular')
    if len(triang_arg.diagonal().nonzero()[0]):
        raise Exception('Matrix is singular')

    triang = mtx(triang_arg.copy())
    n = triang.shape[0]

    unitriang_maker = mtx(I(n)) / triang.diagonal()
    unitriang = unitriang_maker * triang
    nilpotent = unitriang - I(n)

    unitriang_inverse = mtx(I(n))
    for i in xrange(n-1):
        unitriang_inverse = mtx(I(n)) - nilpotent * unitriang_inverse

    return unitriang_inverse * unitriang_maker
    
    
# test
# make random matrix sample, take it low triangle and up triangle

n = 7
sample = mtx(np.random.random((n, n)))
print(sample)

L = np.tril(sample)
U = np.triu(sample)

# find inversions
L_I = triangular_inversion(L)
U_I = triangular_inversion(U)

# check result
print('Check: L * L_I')
print(L * L_I)
print('Check: L_I * L')
print(L_I * L)
print('Check: U * U_I')
print(U * U_I)
print('Check: U_I * U')
print(U_I * U)