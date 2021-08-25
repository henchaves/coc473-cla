import numpy as np

from algorithms.general import (verificar_positiva_definida, 
                                verificar_simetria, 
                                tem_diagonal_dominante)

def resolve_gauss_seidel(A, b, tol=10**-10):

    if not tem_diagonal_dominante(A):
      raise Exception("Matriz A não tem diagonal dominante.")

    n = A.shape[0]
    
    R = np.inf
    x_new = np.ones(b.shape)

    while (R > tol):
        x_old = x_new
        x_new = np.zeros(b.shape)
        
        for i in range(1, n+1):
            x_new[i-1][0] = (b[i-1][0]- sum([A[i-1][j-1]*x_new[j-1][0] for j in range(1, i)]) - sum([A[i-1][j-1]*x_old[j-1][0] for j in range(i+1, n+1)]))/A[i-1, i-1]
            R = np.linalg.norm(x_new - x_old)/np.linalg.norm(x_new)
            
    return x_new