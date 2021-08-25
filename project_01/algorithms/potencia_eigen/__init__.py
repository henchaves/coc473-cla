import numpy as np

def power_method_eigen(A, tol=10**-10):
    n = A.shape[0]
    print(A)
    R = np.inf
    
    x_new = np.ones((n, 1))
    lambda_new = x_new[0][0]

    count = 0
    historico_R = []

    while (R > tol):
        lambda_old = lambda_new
        y = np.matmul(A, x_new)
        lambda_new = y[0][0]
        x_new = y/lambda_new
        
        R = np.abs(lambda_new-lambda_old)/np.abs(lambda_new)
        count += 1
        historico_R.append(R)
    return lambda_new, x_new, historico_R, count