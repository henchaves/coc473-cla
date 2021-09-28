import numpy as np
from sympy import Symbol, exp, diff

def run_newton_root(constants, x_0, max_tol, max_iter):
  x = Symbol('x')
  c1 = Symbol('c1')
  c2 = Symbol('c2')
  c3 = Symbol('c3')
  c4 = Symbol('c4')
  f = c1*exp(c2*x)+c3*x**c4
  f_deriv = diff(f, x)

  c_dict = {"c1": constants[0], "c2": constants[1], "c3": constants[2], "c4": constants[3]}
  for k in range(1, max_iter+1):
    if k == 1:
        x_old = x_0
        
    x_k = x_old - float(f.subs({"x": x_old} | c_dict))/float(f_deriv.subs({"x": x_old} | c_dict))
    tolk = np.abs(x_k - x_old)
    x_old = x_k

    if tolk < max_tol:
        return x_k, k
    if k == max_iter:
        raise Exception("Não convergiu!")
