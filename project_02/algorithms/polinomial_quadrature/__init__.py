import numpy as np
from sympy import Symbol, exp

def get_polinomial_x(a, b):
    polinomial_x = {}

    for N in range(2, 11):
        delta = delta = (b-a)/(N-1)
        polinomial_x[N] = {}

        for i in range(1, N+1):
            if i == 1:
                polinomial_x[N][i] = a
            elif i == N:
                polinomial_x[N][i] = b
            else:
                polinomial_x[N][i] = a + (i-1)*delta
    
    return polinomial_x

def get_polinomial_weights():
    polinomial_weights = {}
    
    for N in range(2, 11):
        polinomial_weights[N] = {}
        A = np.empty((N, N))
        B = np.empty((N, 1))
        x = np.empty((N, 1))
        delta = 1/(N-1)

        for i in range(1, N+1):
            x[i-1][0] = (i-1)*delta

        for i in range(1, N+1):
            for j in range(1, N+1):
                A[i-1][j-1] = x[j-1]**(i-1)
            B[i-1][0] = 1/i
        
        w = np.dot(np.linalg.inv(A), B)
        
        for i in range(1, N+1):
            polinomial_weights[N][i] = w[i-1][0]
    return polinomial_weights

def run_polinomial_quadrature(constants, a, b, N):
  x = Symbol("x")
  c1 = Symbol('c1')
  c2 = Symbol('c2')
  c3 = Symbol('c3')
  c4 = Symbol('c4')
  c_dict = {"c1": constants[0], "c2": constants[1], "c3": constants[2], "c4": constants[3]}
  f = c1*exp(c2*x)+c3*x**c4
  polinomial_x = get_polinomial_x(a, b)
  polinomial_weights = get_polinomial_weights()

  area = 0

  L = b - a
  for i in range(1, N+1):
    w_i = polinomial_weights[N][i]*L
    x_i = polinomial_x[N][i]
    f_i = float(f.subs({"x": x_i} | c_dict))
    area += f_i*w_i
  
  return area