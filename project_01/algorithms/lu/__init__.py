import numpy as np

def decomposicao_lu(A):
    n = A.shape[0]

    L = np.eye(n, dtype=np.double)
    
    for i in range(n):
        factor = A[i+1:, i]/A[i, i]
        L[i+1:, i] = factor
        A[i+1:] = A[i+1:] - factor[:, np.newaxis] * A[i]
    
    return L, A

def resolve_lu(L, U, b):
    n = b.shape[0]
    y = np.zeros((n,1))
    x = np.zeros((n,1))
    
    y[0][0] = b[0][0]/L[0, 0]
    
    for i in range(2, n+1):
        y[i-1][0] = (b[i-1][0] - sum(L[i-1, j-1]*y[j-1][0] for j in range(1, i)))/L[i-1, i-1]

    
    x[n-1][0] = y[n-1][0]/U[n-1, n-1]
    
    for i in reversed(range(1, n)):
        x[i-1][0] = (y[i-1][0] - sum(U[i-1, j-1]*x[j-1][0] for j in range(i+1, n+1)))/U[i-1, i-1] 

    return x