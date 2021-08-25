import numpy as np

from algorithms.general import verificar_simetria

def indices_maximo_valor(A):
    n = A.shape[0]
    
    max_valor = np.NINF
    p, q = (np.nan, np.nan)
    
    
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if np.abs(A[i-1][j-1]) > max_valor:
                max_valor = np.abs(A[i-1][j-1])
                p, q = i, j
    
    return p, q

def calcula_phi(A, p, q):
    if A[p-1][p-1] == A[q-1][q-1]:
        phi = np.pi/4
    else:
        phi = np.arctan(2*A[p-1][q-1]/(A[p-1][p-1]-A[q-1][q-1]))/2
    return phi

def cria_matriz_p(phi, n, p, q):
    P = np.eye(n, n)
    
    P[p-1][p-1] = np.cos(phi)
    P[p-1][q-1] = -np.sin(phi)
    P[q-1][p-1] = np.sin(phi)
    P[q-1][q-1] = np.cos(phi)
    
    return P

def checar_tol(A, tol):
    return np.all([np.abs(A[i-1][j-1]) < tol for i in range(1, A.shape[0]+1) for j in range(1, A.shape[0]+1) if i != j])

def jacob_eigen(A, tol=10**-10):
    
    if not verificar_simetria(A):
        raise Exception("Matriz A não é simétrica.")
    
    n = A.shape[0]
    
    X = np.eye(*A.shape)
    
    while True:
        p, q = indices_maximo_valor(A)
        phi = calcula_phi(A, p, q)
        P = cria_matriz_p(phi, n, p, q)
        
        A = np.matmul(P.T, A)
        A = np.matmul(A, P)
        
        X = np.matmul(X, P)
        
        if checar_tol(A, tol):
            return np.diagonal(A), X