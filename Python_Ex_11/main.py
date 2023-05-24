import ChannelCapacity
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

SNR_dB = np.arange(-20, 20, 1) # dB

SNR = np.power(10, SNR_dB/10)

# A)
# capacity of the Gaussian additive channel with continuous-input, continuous-output
C = ChannelCapacity.Capacity_AGN(SNR)
plt.plot(SNR_dB, C)

# B)
# capacity of the Gaussian additive channel with antipodal signalling and HD
p = 0.5*erfc(np.sqrt(SNR))
C = 1 - ChannelCapacity.H_rondo(p)
plt.plot(SNR_dB, C)

# C)
# capacity of the Gaussian additive channel with antipodal signalling and SD
n_iter = len(SNR)
C = np.zeros(n_iter)
n0 = 1

for i in range(n_iter):
    C[i] = ChannelCapacity.Capacity_AWGN(SNR[i], n0)

plt.plot(SNR_dB, C)

plt.xlabel('Ex/No [dB]')
plt.ylabel('C [infobit/ch.use]')
plt.title('Channel capacity')
plt.ylim(0,1.1)
plt.legend(('continuous-input, continuous-output',
            'antipodal signalling and HD',
            'antipodal signalling and SD'))
plt.hlines(1,-20, 20, linestyles='dashed', colors='k')
plt.show()