def mygcd (a,b):
    """
    This function evaluates the gcd(greatest common divisor) with
    the Euclidian algorithm between the two integers a and b.
    
    Giacomo Di Roberto, February 2022, version 1.0

    """
    
    r0 = a
    r1 = b
    r2 = 1

    while r2 != 0:
        r2 = r0%r1
        r0 = r1
        r1 = r2
    
    return r0
