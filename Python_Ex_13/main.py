import random as rd

def genBit(p: float):
    """
    Generates a random bit. p is the probability of getting a '1'.

    """

    b = rd.random()
    if b > p:
        data = '1'
    else:
        data = '0'
    
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

def encoder(x:str):

    x_3 = ''
    for i in x:
        x_3 += i*3
    
    return x_3

def decoder(y_3:str):

    decoding_rule = {'000': '0',
                     '001': '0',
                     '010': '0',
                     '100': '0',
                     '011': '1',
                     '101': '1',
                     '110': '1',
                     '111': '1'}
    
    y = y_3.replace(y_3, decoding_rule[y_3])

    return(y)


# length of the sequence
N = 5000
nerrors = 0

for i in range(N):
    x = genBit(0.5)
    x_3 = encoder(x)

    y_3 = BSC(x_3, 0.3)
    y = decoder(y_3)

    nerrors += countError(x,y)

print('Number of errors = ', nerrors)
print('BER = ', nerrors/N)




