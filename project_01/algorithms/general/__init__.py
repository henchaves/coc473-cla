import numpy as np

def verificar_simetria(A):
    if (A == A.T).all():
        return True
    else:
        return False

def verificar_positiva_definida(A):
    if np.all(np.linalg.eigvals(A) > 0):
        return True
    else:
        return False

def tem_diagonal_dominante(A):
    D = np.diag(np.abs(A))
    S = np.sum(np.abs(A), axis=1) - D
    print(D)
    print(S)
    if np.all(D > S):
        return True
    else:
        return False