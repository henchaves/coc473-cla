import numpy as np
from sympy import Symbol

def regressao_multilinear(x_arr, y_arr, grau=1):
    x = Symbol('x')
    
    n = x_arr.shape[0]
    
    P = np.empty((n, grau+1))

    for i in range(grau+1):
        P[:, i] =  np.power(x_arr.ravel(), i)
    
    A = np.matmul(P.T, P)
    C = np.matmul(P.T, y_arr)
    b = np.round(np.matmul(np.linalg.inv(A), C), 3)
    
    fn = 0
    for i in range(b.shape[0]):
        fn += x ** i * b[i][0]
    
    return (fn, lambda x_value: float(fn.subs(x, x_value)))