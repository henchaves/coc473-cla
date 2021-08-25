import numpy as np

from algorithms.general import (verificar_positiva_definida, 
                                verificar_simetria, 
                                tem_diagonal_dominante)

def resolve_gauss_seidel(A, b, tol=10**-10):
  if not tem_diagonal_dominante(A):
    raise Exception("Matriz A não tem diagonal dominante.")
  n = A.shape[0]
  
  R = np.inf
  x_new = np.ones((n, 1))
  count = 0
  historico_R = []

  while (R > tol):
    if count > 1000:
      raise Exception("Número de iterações ultrapassou 1000.")
    x_old = x_new.copy()
    x_new = np.zeros((n, 1))
    
    for i in range(1, n+1):
      x_new[i-1][0] = (b[i-1][0]- sum([A[i-1][j-1]*x_new[j-1][0] for j in range(1, i)]) - sum([A[i-1][j-1]*x_old[j-1][0] for j in range(i+1, n+1)]))/A[i-1, i-1]
      R = np.linalg.norm(x_new - x_old)/np.linalg.norm(x_new)
    historico_R.append(R)
    count += 1

  return x_new, historico_R, count