import numpy as np

def rectangular(a,b,N,function):
    """
    Evaluate the integral from a to b of a given function with the rectangular rule.
    N is the number of points.

    Giacomo Di Roberto, May 2023, version 1.1

    """

    delta = (b-a)/N
    x = np.arange(a,b,delta)
    y = function(x)

    result = sum(y)*delta

    return result

def trapezoidal(a,b,N,function):
    """
    Evaluate the integral from a to b of a given function with the trapezoidal rule.
    N is the number of points.  

    Giacomo Di Roberto, May 2023, version 1.1

    """

    delta = (b-a)/N
    x = np.arange(a,b,delta)
    y = function(x)

    result = ( ((y[0] + y[-1])/2) + sum(y,1))*delta

    return result

