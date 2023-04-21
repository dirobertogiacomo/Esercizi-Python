import matplotlib.pyplot as plt
import numpy as np
from math import log2

# graph of I(x)
x = np.arange(0.001, 1.001, 0.001)
I = -np.log2(x)

plt.figure()
plt.xlabel('p(x)')
plt.ylabel('I(x) [Sh]')
plt.title('Information of an event x')
plt.plot(x,I)

# graph of H(p)
p = x[0:-1] # to avoid a division by zero
H = -p*np.log2(p) - (1-p)*np.log2(1-p)

plt.figure()
plt.plot(p, H)
plt.xlabel('p')
plt.ylabel('H(p) [Sh]')
plt.title('Entropy of a Bernoulli\'s random variable ')
plt.xticks([0, 0.5, 1])
plt.show()