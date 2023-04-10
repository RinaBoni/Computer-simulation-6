import random as rand
import numpy as np

def MCint (f, a, b, n):
    s = 0
    for i in range (n):
        x = rand.uniform(a,b)
        s += f(x)
    I = (float(b-a)/n)*s
    return I

def MCint_vec (f, a, b, n):
    x = np.uniform(a, b, n)
    s = sum(f(x))
    I = (float(b-a)/n)*s
    return I

def MCint2 (f, a, b, n):
    s = 0
    I = zeros(n)
    for k in range(1, n+1):
        x = np.uniform(a, b)
        s += f(x)
        I[k-1] = (float(b-a)/k)*s
    return I


