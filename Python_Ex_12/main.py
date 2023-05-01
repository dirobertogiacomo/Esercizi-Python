import random as rd

def genData(N: int, p: float):
    """
    Generates a random sequence of N bits. p is the probability of getting a '1'.

    """
    
    data = ''

    for i in range(N):
        b = rd.random()
        if b > p:
            data += '1'
        else:
            data += '0'
    
    return data

def BSC(x:str, p: float):
    """
    Function to simulate a Binary Symmetric Channel.
    
    Parameters
    ----------
    x : string
        Input sequence
    
    p : float in interval [0;1]
        Error probability

    Return
    ------
    y : string
        Output sequence

    """

    y = ''

    for b in x:
        if b == '0':
            if rd.random() > p:
                y += '0'
            else:
                y += '1'
        else:
            if rd.random() > p:
                y += '1'
            else:
                y += '0'
    
    return y

def countError(x, y):
    """
    Counts the number of errors between two sequence of bits
    
    """

    if x != y:
        n = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                n += 1
    else:
        return 0
    
    return n


# length of the sequence
N = 1024

x = genData(N, 0.5)

y = BSC(x, 0.3)

nerrors = countError(x,y)

print('x = ', x)
print('y = ', y)
print('Number of errors = ', nerrors)
print('BER = ', nerrors/N)
