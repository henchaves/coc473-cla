import numpy as np
import pandas as pd
from sympy import Symbol, diff, sin


def get_runge_kutta_nystrom(f, delta, y_0, dy_0, maximum_t = 1):
    y_arr = []
    y_arr.append(y_0)
    
    dy_arr = [] 
    dy_arr.append(dy_0)
    
    t_ = 0
    i = 0
    
    results = []
    results.append([t_, y_0, dy_0])
    
    while (t_ < maximum_t):
        K_1 = delta/2 * float(f.subs({"t": t_, "y": y_arr[i], "dy": dy_arr[i]}))
        Q = delta/2 * (dy_arr[i] + K_1/2)
        
        K_2 = delta/2 * float(f.subs({"t": t_ + delta/2, "y": y_arr[i] + Q, "dy": dy_arr[i] + K_1}))
        K_3 = delta/2 * float(f.subs({"t": t_ + delta/2, "y": y_arr[i] + Q, "dy": dy_arr[i] + K_2}))
        L = delta * (dy_arr[i] + K_3)
        
        K_4 = delta/2 * float(f.subs({"t": t_ + delta, "y": y_arr[i] + L, "dy": dy_arr[i] + 2*K_3}))
        
        y_new = y_arr[i] + delta * (dy_arr[i] + (K_1 + K_2 + K_3)/3)
        print(y_new)
        y_arr.append(y_new)
        
        dy_new = dy_arr[i] + (K_1 + 2*K_2 + 2*K_3 + K_4)/3
        dy_arr.append(dy_new)
        
        i += 1
        t_ = delta * i
        
        results.append([t_, y_new, dy_new])
    return results

def run_runge_kutta_nystrom(delta, maximum_t, c_dict):
    m = Symbol("m")
    c = Symbol("c")
    k = Symbol("k")

    a1 = Symbol("a1")
    a2 = Symbol("a2")
    a3 = Symbol("a3")
    w1 = Symbol("w1")
    w2 = Symbol("w2")
    w3 = Symbol("w3")

    t = Symbol("t")
    y = Symbol("y")
    dy = Symbol("dy")

    f = (a1*sin(w1*t)+a2*sin(w2*t)+a3*sin(w3*t) - c*dy - k*y)/m
    f = f.subs(c_dict)
    # print(f)

    y_0 = 0
    dy_0 = 0

    results = get_runge_kutta_nystrom(f, delta, y_0, dy_0, maximum_t)
    results_new = [[a[0], a[1], a[2], f.subs({"t": a[0], "y": a[1], "dy": a[2]})] for a in results]
    # return results_new
    df = pd.DataFrame(results_new, columns=["tempo", "deslocamento", "velocidade", "aceleração"])
    return df