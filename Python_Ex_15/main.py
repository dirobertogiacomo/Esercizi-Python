import numpy as np
import random
from scipy.special import erfc
import matplotlib.pyplot as plt
from scipy.special import binom

def genBit(p: float):
    """
    Generates a random bit. p is the probability of getting a '1'.

    Giacomo Di Roberto, May 2023, version 1.0

    """

    b = random.random()
    if b >= p:
        return '1'
    else:
        return '0'

def BSC(x, p: float):
    """
    Function to simulate a Binary Symmetric Channel.
    
    Parameters
    ----------
    x : np.array
        Input sequence
    
    p : float in interval [0;1]
        Error probability

    Return
    ------
    y : np.array
        Output sequence
    
    Giacomo Di Roberto, May 2023, version 1.0

    """

    N = len(x)

    y = np.zeros(N, dtype=int)

    for i in range(N):
        if x[i] == 0:
            if random.random() > p:
                y[i] = 0
            else:
                y[i] = 1
        else:
            if random.random() > p:
                y[i] = 1
            else:
                y[i] = 0
    
    return y

def Hamming_encoder(x):
    """
    Perform a channel encoder for Hamming code (7,4).

    Giacomo Di Roberto, May 2023, version 1.0

    """

    # generator matrix
    G = np.array([[1,0,0,0,1,0,1],
                  [0,1,0,0,1,1,1],
                  [0,0,1,0,1,1,0],
                  [0,0,0,1,0,1,1]], dtype=int)
    
    c = x @ G

    c[c%2 == 0] = 0
    c[c%2 == 1] = 1

    return c

def Hamming_decoder(y):
    """
    Perform a channel decoder for Hamming code (7,4).

    Giacomo Di Roberto, May 2023, version 1.0
    
    """

    H = np.array([[1,1,1,0,1,0,0],
                  [0,1,1,1,0,1,0],
                  [1,1,0,1,0,0,1]], dtype=int)
    
    decoding_table = {tuple(np.array([0,0,0],dtype=int)): np.array([0,0,0,0,0,0,0],dtype=int),
                      tuple(np.array([0,0,1],dtype=int)): np.array([0,0,0,0,0,0,1],dtype=int),
                      tuple(np.array([0,1,0],dtype=int)): np.array([0,0,0,0,0,1,0],dtype=int),
                      tuple(np.array([1,0,0],dtype=int)): np.array([0,0,0,0,1,0,0],dtype=int),
                      tuple(np.array([0,1,1],dtype=int)): np.array([0,0,0,1,0,0,0],dtype=int),
                      tuple(np.array([1,1,0],dtype=int)): np.array([0,0,1,0,0,0,0],dtype=int),
                      tuple(np.array([1,0,1],dtype=int)): np.array([1,0,0,0,0,0,0],dtype=int),
                      tuple(np.array([1,1,1],dtype=int)): np.array([0,1,0,0,0,0,0],dtype=int)}
    
    s = y @ np.transpose(H)

    s[s%2 == 0] = 0
    s[s%2 == 1] = 1

    e = decoding_table[tuple(s)]

    c = y + e

    c[c%2 == 0] = 0
    c[c%2 == 1] = 1

    # string conversion
    c = np.array2string(1*c, separator='').replace('[', '').replace(']', '')

    return c

def countError(x, y):
    """
    Counts the number of errors between two sequence of bits

    Giacomo Di Roberto, May 2023, version 1.0
    
    """

    if x != y:
        n = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                n += 1
    else:
        return 0
    
    return n


SNR_dB = np.arange(0, 11, 1)

SNR = np.power(10, SNR_dB/10)

Rc = 4/7
ER = np.zeros(len(SNR))
BER = np.zeros(len(SNR))

p = 0.5*erfc(np.sqrt(SNR*Rc))

# computing theorical error probability for BSC
Peb_theor_unc = 0.5*erfc(np.sqrt(SNR))
Peb_theor = 9*(p**2)*((1-p)**5)
Pe_theor = binom(7,2)*(p**2)*((1-p)**5)

N_e_max = 100
N_iter_max = 5000

for i in range(len(SNR)):

    N_e = 0
    N_eb = 0
    N_iter = 0

    while (N_e < N_e_max and N_iter < N_iter_max):

        # generation of a 4 bits sequence
        x = np.zeros(4, dtype=int)

        for j in range(4):
            b = genBit(0.5)
            x[j] = int(b)

        # channel coding (Hamming)
        c = Hamming_encoder(x)

        # BSC
        y = BSC(c, p[i])

        # ML decoder 
        d = Hamming_decoder(y) # decoded codewords
        r = d[0:4] # recived bits

        # check for errors
        x = np.array2string(1*x, separator='').replace('[', '').replace(']', '') # string conversion
        c = np.array2string(1*c, separator='').replace('[', '').replace(']', '') # string conversion

        if c != d: 
            N_e += 1
            N_eb += countError(x,r)

        N_iter += 1
    
    ER[i] = N_e/N_iter
    BER[i] = N_eb/(4*N_iter)

# plot
plt.plot(SNR_dB, (Peb_theor))
plt.plot(SNR_dB, (Peb_theor_unc))
plt.plot(SNR_dB, (BER))
plt.yscale('log')
plt.xlabel('Eb/N0 [dB]')
plt.ylabel('BER')
plt.title('Bit Error Rate')
plt.legend(('Theoretical','Uncoded','Simulated'))

plt.figure()
plt.plot(SNR_dB, Pe_theor)
plt.plot(SNR_dB, ER)
plt.xlabel('Eb/N0 [dB]')
plt.ylabel('ER')
plt.title('Error Rate')
plt.legend(('Theoretical','Simulated'))
plt.yscale('log')

plt.show()