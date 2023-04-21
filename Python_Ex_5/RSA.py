import random


### source: https://www.geeksforgeeks.org/solovay-strassen-method-of-primality-test/ 
  
def modulo(base, exponent, mod):
    """
    modulo function to perform binary 
    exponentiation

    """ 

    x = 1; 
    y = base; 
    while (exponent > 0): 
        if (exponent % 2 == 1): 
            x = (x * y) % mod; 
  
        y = (y * y) % mod; 
        exponent = exponent // 2; 
  
    return x % mod; 
  
def calculateJacobian(a, n):
    """
    To calculate Jacobian symbol of a
    given number 

    """ 

    if (a == 0): 
        return 0;# (0/n) = 0 
  
    ans = 1; 
    if (a < 0): 
          
        # (a/n) = (-a/n)*(-1/n) 
        a = -a; 
        if (n % 4 == 3): 
          
            # (-1/n) = -1 if n = 3 (mod 4) 
            ans = -ans; 
  
    if (a == 1): 
        return ans; # (1/n) = 1 
  
    while (a): 
        if (a < 0):
              
            # (a/n) = (-a/n)*(-1/n) 
            a = -a; 
            if (n % 4 == 3):
                  
                # (-1/n) = -1 if n = 3 (mod 4) 
                ans = -ans; 
  
        while (a % 2 == 0): 
            a = a // 2; 
            if (n % 8 == 3 or n % 8 == 5): 
                ans = -ans; 
  
        # swap 
        a, n = n, a; 
  
        if (a % 4 == 3 and n % 4 == 3): 
            ans = -ans; 
        a = a % n; 
  
        if (a > n // 2): 
            a = a - n; 
  
    if (n == 1): 
        return ans; 
  
    return 0; 

def solovayStrassen(p, iterations): 
    """
    To perform the Solovay- Strassen Primality Test

    """
  
    if (p < 2): 
        return False; 
    if (p != 2 and p % 2 == 0): 
        return False; 
  
    for i in range(iterations):
          
        # Generate a random number a 
        a = random.randrange(p - 1) + 1; 
        jacobian = (p + calculateJacobian(a, p)) % p; 
        mod = modulo(a, (p - 1) / 2, p); 
  
        if (jacobian == 0 or mod != jacobian): 
            return False; 
  
    return True

###

def gcdExtended(a, b):
    """
    function for extended Euclidean Algorithm.

    source : https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/

    """
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y


def RSAKeyGen(pmax):
    """
    This funcion produces e, d and n for the RSA algorithm.

    Giacomo Di Roberto, March 2023, version 1.1

    """
    
    p1 = 4
    p2 = 4

    # finding p1 and p2
    while(solovayStrassen(p1, 20) == False):
        p1 = random.randint(int(pmax/2), pmax)

    while(solovayStrassen(p2, 20) == False):
        p2 = random.randint(1, pmax)

    # evaluating n
    n = p1*p2

    # evaluating φ
    phi = (p2-1)*(p1-1)

    # finding e such that gcd(e,φ) = 1
    d = -1
    while d < 0:
        gcd = 0

        while(gcd != 1):
            e = random.randint(1, pmax)
            gcd,x = gcdExtended(e,phi)[0:2]

        # finding d
        d = x

    return e,d,n


def RSAEncoder(e,n,M):
    """
    This function encrypt the message M whith the RSA method

    Giacomo Di Roberto, March 2023, version 1.1

    """

    # binary representation of e
    eb = bin(e).replace('0b', '')

    # encription
    l = len(eb)
    C = 1
    for i in range(l):
        C = (C*C)%n
        if(eb[i] == '1'):
            C = (C*M)%n
    
    return C

def RSADecoder(d,n,C):
    """
    This function decrypts the encryoted message C with the RSA method
    
    Giacomo Di Roberto, March 2023, version 1.1

    """

    # binary representation of d
    db = bin(d).replace('0b', '')

    # decription
    l = len(db)
    M = 1
    for i in range(l):
        M = (M*M)%n
        if(db[i] == '1'):
            M = (M*C)%n
    
    return M
