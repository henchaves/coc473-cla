import numpy as np

def power_method_eigen(A, tol=10**-5):
    n = A.shape[0]
    print(A)
    R = np.inf
    
    x_new = np.ones((n, 1))
    lambda_new = x_new[0][0]
    
    while (R > tol):
        x_old = x_new
        lambda_old = lambda_new
        y = np.matmul(A, x_new)
        lambda_new = y[0][0]
        x_new = y/lambda_new
        
        R = np.abs(lambda_new-lambda_old)/np.abs(lambda_new)
    
    return lambda_new, x_new