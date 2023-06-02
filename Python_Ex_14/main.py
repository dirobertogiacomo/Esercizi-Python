import numpy as np
import random
import math 
from scipy.special import erfc
import matplotlib.pyplot as plt

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
    Perform the antipodal coding for a single input bit: 0 -> 1 and 1 -> -1.

    Giacomo Di Roberto, May 2023, version 1.0

    """

    if b == '1':
        return '-1'
    
    if b == '0':
        return '1'

def antipodalDecoding(b):
    """
    Perform the antipodal decoding for a single input bit: 1 -> 0 and -1 -> 1.

    Giacomo Di Roberto, May 2023, version 1.0

    """

    if b == '1':
        return '0'
    
    if b == '-1':
        return '1'
    
def gaussianNoise(SNR):
    """
    Return a sample of random Gaussian Noise, with the given SNR = Eb/N0.
    
    Giacomo Di Roberto, May 2023, version 1.0

    """

    sigma = math.sqrt(1/(2*SNR))
    n = random.gauss(0, sigma)

    return n

def threshold_decisor(y):
    """
    Perform a trashold decision on the given bit.
    
    Giacomo Di Roberto, May 2023, version 1.0

    """

    if y >= 0:
        return '1' 
    else:
        return '-1'


SNR_dB = np.arange(0, 11, 1)

SNR = np.power(10, SNR_dB/10)

simulated_BER = np.zeros(len(SNR))
analytical_BER = 0.5*erfc(np.sqrt(SNR))

N_err_max = 100
iter_max = 1000000

for i in range(len(SNR)):

    N_err = 0
    iter = 0

    print('Simulating Eb/N0 = ', SNR_dB[i], ' dB')

    while (N_err < N_err_max and iter < iter_max):

        # generation of a bit
        b = genBit(0.5)

        # antipodal coding
        x = antipodalCoding(b)

        # noise
        y = int(x) + gaussianNoise(SNR[i])

        # hard decision
        d = threshold_decisor(y)

        # antipodal decoding
        r = antipodalDecoding(d)
        
        # check for errors
        if r != b:
            N_err += 1

        iter += 1
    
    simulated_BER[i] = N_err/iter


plt.plot(SNR_dB, analytical_BER)
plt.plot(SNR_dB, simulated_BER)
plt.xlabel('Eb/N0 [dB]')
plt.ylabel('BER')
plt.title('Bit Error Rate')
plt.legend(('Analytical', 'Simulated'))
plt.yscale('log')

plt.savefig('Python_Ex_14/Bit error rate.png')
plt.show()

