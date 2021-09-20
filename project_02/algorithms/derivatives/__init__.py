import numpy as np
from sympy import Symbol, exp

def deriv_central(constants, x_value, delta_x):
    x = Symbol("x")
    c1 = Symbol('c1')
    c2 = Symbol('c2')
    c3 = Symbol('c3')
    c4 = Symbol('c4')
    c_dict = {"c1": constants[0], "c2": constants[1], "c3": constants[2], "c4": constants[3]}
    f = c1*exp(c2*x)+c3*x**c4
    x_mais = x_value + delta_x
    f_mais = float(f.subs({"x": x_mais} | c_dict))
    x_menos = x_value - delta_x
    f_menos = float(f.subs({"x": x_menos} | c_dict))
    
    f_deriv = (f_mais - f_menos)/(2*delta_x)
    return f_deriv

def deriv_frente(constants, x_value, delta_x):
    x = Symbol("x")
    c1 = Symbol('c1')
    c2 = Symbol('c2')
    c3 = Symbol('c3')
    c4 = Symbol('c4')
    c_dict = {"c1": constants[0], "c2": constants[1], "c3": constants[2], "c4": constants[3]}
    f = c1*exp(c2*x)+c3*x**c4
    x_mais = x_value + delta_x
    f_mais = float(f.subs({"x": x_mais} | c_dict))
    f_normal = float(f.subs({"x": x_value} | c_dict))
    
    f_deriv = (f_mais - f_normal)/delta_x
    return f_deriv

def deriv_tras(constants, x_value, delta_x):
    x = Symbol("x")
    c1 = Symbol('c1')
    c2 = Symbol('c2')
    c3 = Symbol('c3')
    c4 = Symbol('c4')
    c_dict = {"c1": constants[0], "c2": constants[1], "c3": constants[2], "c4": constants[3]}
    f = c1*exp(c2*x)+c3*x**c4
    f_normal = float(f.subs({"x": x_value} | c_dict))
    x_menos = x_value - delta_x
    f_menos = float(f.subs({"x": x_menos} | c_dict))
    
    f_deriv = (f_normal - f_menos)/delta_x
    return f_deriv

def deriv_richard(constants, x_value, delta_x_1, delta_x_2):
    d_1 = deriv_frente(constants, x_value, delta_x_1)
    d_2 = deriv_frente(constants, x_value, delta_x_2)
    q = delta_x_1/delta_x_2
    
    f_deriv = d_1 + (d_1-d_2)/(np.power(q, -1) - 1)
    return f_deriv