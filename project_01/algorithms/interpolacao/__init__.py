import numpy as np
from sympy import Symbol

def calcula_phi(x_arr, i, n, x):
    
    numerator = 1
    denominator = 1
    
    for k in range(1, n+1):
        if k != i:
            numerator *= (x-x_arr[k-1][0])
            denominator *= (x_arr[i-1][0] - x_arr[k-1][0])
            
    return numerator/denominator

def interpolacao_lagrange(x_arr, y_arr):
    x = Symbol('x')

    n = x_arr.shape[0]
    phi_arr = np.zeros(n, dtype="object")
    fn = 0
    
    for i in range(1, n+1):
        phi_arr[i-1] = calcula_phi(x_arr, i, n, x)
        fn += phi_arr[i-1]*y_arr[i-1][0]
        
    return (fn, lambda x_value: float(fn.subs(x, x_value)))