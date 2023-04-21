def mybemodn (b,e,n):
    """
    This function computes b^e mod n iteratively as c=(b c) mod n.
    
    Giacomo Di Roberto, February 2022, version 1.0

    """
     
    c = 1
    b = b%n

    for i in range(e):
        c = (b*c)%n
    
    return c
