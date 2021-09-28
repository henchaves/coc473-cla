import numpy as np
from sympy import Symbol, exp

def run_bisseccao(constants, a, b, max_tol, max_iter):
  x = Symbol('x')
  c1 = Symbol('c1')
  c2 = Symbol('c2')
  c3 = Symbol('c3')
  c4 = Symbol('c4')
  f = c1*exp(c2*x)+c3*x**c4

  c_dict = {"c1": constants[0], "c2": constants[1], "c3": constants[2], "c4": constants[3]}
  count = 0
  while np.abs(b-a) > max_tol:
    x_i = (a+b)/2
    f_i = f.subs(c_dict | {"x": x_i})
    if (f_i > 0):
        b = x_i
    else:
        a = x_i
    if count == max_iter:
      raise Exception("Não convergiu!")
    count += 1

  return x_i, count