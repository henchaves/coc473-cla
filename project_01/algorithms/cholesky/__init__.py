import numpy as np

def decomposicao_cholesky(A):
    n = A.shape[0]

    L = np.zeros((n, n))

    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k):
                L[i][i] = np.sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L

def resolve_cholesky(L, b):
    n = b.shape[0]
    y = np.zeros((n,1))
    x = np.zeros((n,1))
    
    y[0][0] = b[0][0]/L[0, 0]
    
    for i in range(2, n+1):
        y[i-1][0] = (b[i-1][0] - sum(L[i-1, j-1]*y[j-1][0] for j in range(1, i)))/L[i-1, i-1]

    
    x[n-1][0] = y[n-1][0]/L.T[n-1, n-1]
    
    for i in reversed(range(1, n)):
        x[i-1][0] = (y[i-1][0] - sum(L.T[i-1, j-1]*x[j-1][0] for j in range(i+1, n+1)))/L.T[i-1, i-1] 
    
    return x