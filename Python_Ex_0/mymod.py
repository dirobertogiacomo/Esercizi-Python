def mymod (a,b):
    """
    The function evaluates the quotient q and the remainder r
    of the division between a and b, by successive subctractions.
    a and b are positive integers. 
    
    Giacomo Di Roberto, February 2022, version 1.0

    """
      
    q = 0
    while a >=b:
        a = a-b
        q = q+1
    return q,a
