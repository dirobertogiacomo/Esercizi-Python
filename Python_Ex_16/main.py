import numpy as np
import random
import math 
from scipy.special import erfc
import matplotlib.pyplot as plt
import time

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

def antipodalCoding(b):
    """
    Perform the antipodal coding to the given input: 0 -> 1 and 1 -> -1.

    Giacomo Di Roberto, May 2023, version 1.1

    """

    coded = b.copy()

    coded[b == 1] = -1
    coded[b == 0] = 1
    

    return coded

def antipodalDecoding(coded):
    """
    Perform the antipodal decoding to the given input: 1 -> 0 and -1 -> 1.

    Giacomo Di Roberto, May 2023, version 1.1

    """
    
    decoded = coded.copy()

    decoded[coded == 1] = 0
    decoded[coded == -1] = 1
    
    return decoded


def Hamming_encoder(x):
    """
    Perform a channel encoder for Hamming code (7,4).

    Giacomo Di Roberto, May 2023, version 1.0

    """

    # generator matrix
    G = np.array([[1,0,0,0,1,0,1],
                  [0,1,0,0,1,1,1],
                  [0,0,1,0,1,1,0],
                  [0,0,0,1,0,1,1]],dtype=int)
    
    c = x @ G

    c[c%2 == 0] = 0
    c[c%2 == 1] = 1

    return c

def Hamming_decoder(y):
    """
    Perform a channel decoder for Hamming code (7,4).

    Giacomo Di Roberto, May 2023, version 1.0
    
    """

    # set of codewords encoded with antipodal coding
    codewords = np.array([[ 1., 1., 1., 1., 1., 1., 1.],
                          [ 1., 1., 1.,-1., 1.,-1.,-1.],
                          [ 1., 1.,-1., 1.,-1.,-1., 1.],
                          [ 1.,-1., 1., 1.,-1.,-1.,-1.],
                          [-1., 1., 1., 1.,-1., 1.,-1.],
                          [ 1., 1.,-1.,-1.,-1., 1.,-1.],
                          [ 1.,-1., 1.,-1.,-1., 1., 1.],
                          [-1., 1., 1.,-1.,-1.,-1., 1.],
                          [ 1.,-1.,-1., 1., 1., 1.,-1.],
                          [-1., 1.,-1., 1., 1.,-1.,-1.],
                          [-1.,-1., 1., 1., 1.,-1., 1.],
                          [-1.,-1.,-1., 1.,-1., 1., 1.],
                          [ 1.,-1.,-1.,-1., 1.,-1., 1.],
                          [-1., 1.,-1.,-1., 1., 1., 1.],
                          [-1.,-1., 1.,-1., 1., 1.,-1.],
                          [-1.,-1.,-1.,-1.,-1.,-1.,-1.]])

    corr = y*codewords.copy()
    corr = np.sum(corr, axis=1)

    l = np.argmax(corr)

    c = codewords[l, :]

    return c

def gaussianNoise(SNR):
    """
    Return a sample of random Gaussian Noise, with the given SNR = (Eb*Rc)/N0.
    
    Giacomo Di Roberto, May 2023, version 1.0

    """

    sigma = math.sqrt(1/(2*SNR))
    n = random.gauss(0, sigma)

    return n

def countError(x, y):
    """
    Counts the number of errors between two sequence of bits

    Giacomo Di Roberto, May 2023, version 1.1
    
    """
    
    errors = np.where(x != y)
    n = len(errors[0])
    
    return n


SNR_dB = np.arange(0, 11, 1)

SNR = np.power(10, SNR_dB/10)

Rc = 4/7
BER = np.zeros(len(SNR))

# computing theorical error probability 
Peb_theor_SD = (3/2)*erfc(np.sqrt(SNR*(12/7)))

p = 0.5*erfc(np.sqrt(SNR*Rc))
Peb_theor_HD = 9*(p**2)*((1-p)**5)


N_e_max = 100
N_iter_max = 2e6

start  = time.time()
for i in range(len(SNR)):

    N_e = 0
    N_eb = 0
    N_iter = 0

    print('Simulating Eb/N0 = ', SNR_dB[i], ' dB')

    while (N_e < N_e_max and N_iter < N_iter_max):

        # generation of a 4 bits sequence
        x = np.zeros(4, dtype=float)

        for j in range(4):
            b = genBit(0.5)
            x[j] = bool(float(b))

        # channel coding (Hamming)
        c = Hamming_encoder(x)

        # antipodal coding
        y = antipodalCoding(c)

        # noise
        k = SNR[i]*Rc
        for j in range(7):
            y[j] += gaussianNoise(k)

        # decoder 
        d = Hamming_decoder(y) # decoded codewords
        
        # antipodal decoding
        d = antipodalDecoding(d)
        r = d[0:4] # recived bits

        # check for errors
        if (True in (c !=d)):
            N_e += 1
            N_eb += countError(x,r)
        
        N_iter += 1
    
    BER[i] = N_eb/(4*N_iter)

stop = time.time()
print('Elapsed time:', stop-start, ' sec')

plt.plot(SNR_dB, (Peb_theor_HD))
plt.plot(SNR_dB, (Peb_theor_SD))
plt.plot(SNR_dB, (BER))
plt.yscale('log')
plt.xlabel('Eb/N0 [dB]')
plt.ylabel('BER')
plt.title('Bit Error Rate')
plt.legend(('Theoretical HD', 'Theoretical SD', 'Simulated SD'))

plt.savefig('Python_Ex_16/Bit error rate.png')
plt.show()
