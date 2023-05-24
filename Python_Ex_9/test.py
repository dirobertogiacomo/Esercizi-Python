import matplotlib.pyplot as plt
import numpy as np
import numIntegration


# defining the function to be integrated
def func(x):

    return x**3


a = 0
b = 15
N = 10000

# rectangular rule
rect = numIntegration.rectangular(a,b,N,func)
print('Rectangular rule: ',rect)

# trapezoidal rule
trap = numIntegration.trapezoidal(a,b,N,func)
print('Trapezoidal rule: ', trap)


