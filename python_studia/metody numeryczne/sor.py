import numpy as np

def sor_solver(A, b, omega, initial_guess, convergence_criteria):
  """
  This is an implementation of the pseduo-code provided in the Wikipedia article.
  Inputs:
    A: nxn numpy matrix
    b: n dimensional numpy vector
    omega: relaxation factor
    initial_guess: An initial solution guess for the solver to start with
  Returns:
    phi: solution vector of dimension n
  """
  phi = initial_guess[:]
  residual = np.linalg.norm(np.matmul(A, phi) - b) #Initial residual
  step = 0
  while residual > convergence_criteria:
    step = step + 1
    for i in range(A.shape[0]):
      sigma = 0
      for j in range(A.shape[1]):
        if j != i:
          sigma += A[i][j] * phi[j]
      phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma)
    residual = np.linalg.norm(np.matmul(A, phi) - b)
    print(str(step) +' Residual: {0:10.6g}'.format(residual))
  return phi




a = [
    [5,1,0],
    [1,2,0],
    [10,0,1]
]
a = np.array(a)

b = [-1,-2,2]
b = np.array(b)

initial_guess = np.zeros(len(a))

#An example case that mirrors the one in the Wikipedia article
residual_convergence = 1e-4
omega = 1.9 #Relaxation factor

phi = sor_solver(a, b, omega, initial_guess, residual_convergence)
for a in phi:
    print('{0:10.4f}'.format(a))