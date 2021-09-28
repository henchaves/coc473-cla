import numpy as np
from sympy import Symbol, diff

def create_F(number_of_functions, functions):
    F = np.array([[functions[i]] for i in range(number_of_functions)])
    return F

def create_J(number_of_functions, number_of_constants, functions):
    J = np.empty((number_of_functions, number_of_constants), dtype=object)
    for i in range(number_of_functions):
        for j in range(number_of_constants):
            J[i][j] = diff(functions[i], f"c{j+2}")
    return J

def update_c_dict(X, extra_dict={}):
    c_dict = {f"c{i+2}":X[i, 0] for i in range(len(X))}
    c_dict.update(extra_dict)
    return c_dict

def sub_F(F, c_dict):
    F = F.copy()
    for i in range(F.shape[0]):
        for j in range(F.shape[1]):
            F[i][j] = F[i][j].subs(c_dict)
    return F.astype(float)

def sub_J(J, c_dict):
    J = J.copy()
    for i in range(J.shape[0]):
        for j in range(J.shape[1]):
            J[i][j] = J[i][j].subs(c_dict)
    return J.astype(float)

def calculate_nl_newton(max_iter, max_tol, X0, theta_dict, F, J):
    X_list = []
    X_list.append(X0)

    for k in range(1, max_iter+1):
        c_dict = update_c_dict(X_list[k-1], theta_dict)
        F_k = sub_F(F, c_dict)
        J_k = sub_J(J, c_dict)
        J_k_inv = np.linalg.inv(J_k)
        delta_X = np.dot(-J_k_inv, F_k)
        X_k = X_list[k-1] + delta_X
        X_list.append(X_k.copy())    
        tolk = np.linalg.norm(delta_X)/np.linalg.norm(X_k)
        if tolk < max_tol:
            return X_k, k

        if k == max_iter:
            raise Exception("Não convergiu")


def run_newton(max_iter, max_tol, X0, theta_dict):
    c2 = Symbol('c2')
    c3 = Symbol('c3')
    c4 = Symbol('c4')
    θ1 = Symbol('θ1')
    θ2 = Symbol('θ2')
    
    f1 = 2*c3**2+c2**2+6*c4**2-1
    f2 = 8*c3**3+6*c3*c2**2+36*c3*c2*c4+108*c3*c4**2-θ1
    f3 = 60*c3**4+60*c3**2*c2**2+576*c3**2*c2*c4+2232*c3**2*c4**2+252*c4**2*c2**2+1296*c4**3*c2+3348*c4**4+24*c2**3*c4+3*c2-θ2
    
    fns = [f1, f2, f3]
    
    number_of_functions = 3
    number_of_constants = 3

    
    F = create_F(number_of_functions, fns)
    J = create_J(number_of_functions, number_of_constants, fns)

    X, k = calculate_nl_newton(max_iter, max_tol, X0, theta_dict, F, J)
    return np.round(X.ravel(), 3).tolist(), k