import numpy as np
import math


def H_rondo(p):
    """
    Evaluate the entropy for a Bernpulli's R.V.

    Giacomo Di Roberto, May 2023, version 1.0

    """
    p[p == 0] = 0.000000001 # avoiding warnings

    return -p*np.log2(p) - (1-p)*np.log2(1-p)

def Capacity_AGN(SNR):
    """
    Evaluate the channel capacity for an AGN channel.

    Giacomo Di Roberto, May 2023, version 1.0

    """

    return 0.5*np.log2(1+(SNR))


def Capacity_AWGN(Ex, n0):
    """
    Evaluate the channel capacity for an AWGN channel.

    Giacomo Di Roberto, May 2023, version 1.0

    """

    def trapezoidal(func, delta):
        """
        Evaluate the integral of a given function y with the trapezoidal rule.

        Giacomo Di Roberto, May 2023, version 1.1

        """

        result = ( ((func[0] + func[-1])/2) + sum(func,1))*delta

        return result

    def error_probability(y, Ex, n0):
        """
        Define the error probability for an AWGN channel.

        Giacomo Di Roberto, May 2023, version 1.0  

        """

        var = n0/2
        sqrtEx = np.sqrt(Ex)

        A = np.exp(- ( (np.power(y - sqrtEx, 2)) / (2*var) ) )
        B = np.exp(- ( (np.power(y + sqrtEx, 2)) / (2*var) ) )
        C = np.sqrt(2*math.pi*var)*2

        return (A+B)/C
    

    # constants
    N = 100000
    sqrtEx = np.sqrt(Ex)
    var = n0/2
    std_dev = math.sqrt(var) # standard deviation
    k = math.sqrt(2*math.pi*math.e*var)

    # interval
    start = -5*std_dev - sqrtEx
    stop = sqrtEx + 5*std_dev
    delta = (stop - start)/N

    y = np.arange(start, stop, delta)

    # error probability
    p = error_probability(y, Ex, n0)
    p[p == 0] = 0.000000001 # avoiding warnings

    # integrand function
    f = p*np.log2(p*k)

    # channel capacity 
    C = -trapezoidal(f,delta)

    return C
    
