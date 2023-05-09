import random as random_number
import matplotlib.pyplot as plt
from numpy import array
import numpy as np


def MCint3(f,a, b, n, N=100):
    s = 0
    I_values = []
    k_values = []

    for k in range(1, n+1):
        x = random_number.uniform(a, b)
        s += f(x)
        if k % N == 0:
            I = (float(b-a)/k)*s
            I_values.append(I)
            k_values.append(k)
    return k_values, I_values


def f1 (x):
    return np.sin(x)/(1+np.sin(x))

k, I = MCint3(f1, 0.8, 1.6, 1000000, N=10000)
error = 6.5 - array(I)

plt.title('Monte Carlo integration')
plt.xlabel('n')
plt.ylabel('error')
plt.plot(k, error)
plt.show()
