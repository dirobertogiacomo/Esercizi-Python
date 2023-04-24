import matplotlib.pyplot as plt
import numpy as np

def rectangular(y, delta):
    """
    Evaluate the integral of a function with the rectangular rule

    """

    result = sum(y)*delta

    return result


def trapezoidal(y, delta):
    """
    Evaluate the integral of a function with the trapezoidal rule

    """


    result = (sum(y, 1)) + (y[0] + y[-1])/2
    result = result*delta
    
    return result

x = np.arange(0,5,0.001)

y = x**2

delta = x[1] - x[0]

z = rectangular(y,delta)
j = trapezoidal(y,delta)

print(z)
print(j)

plt.plot(x,y)
plt.show()
