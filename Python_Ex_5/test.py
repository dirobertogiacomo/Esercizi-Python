import RSA
import random as rd

# key generation
pmax = rd.randint(10e5, 10e15)
e,d,n = RSA.RSAKeyGen(pmax)

print('e = ', e, '\nd = ', d, '\nn = ', n)

# message
M = rd.randint(100, n)
print('Message = ', M)

# encoding
C = RSA.RSAEncoder(e,n,M)
print('Ciphered message = ', C)

# decoding
D = RSA.RSADecoder(d,n,C)
print('Decoded message = ', D)

if D == M:
    print('The message has been successfully decoded!\n')
    
