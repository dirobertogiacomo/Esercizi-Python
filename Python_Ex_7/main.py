import cryptoFunctions as crf
import matplotlib.pyplot as plt
import pandas as pd
from math import log2

text = crf.textConverter(open('Python_Ex_7/text_it.txt').read(), space=True)

# frequency analysis
freqData = pd.DataFrame(crf.freqAnalysis(text, space=True))

# plot
plt.figure()
plt.bar('Letter','Frequence', data=freqData)

# evaluating the entropy
p = freqData['Frequence']/100
H = 0
for i in range(len(p)):
    if p[i] != 0:
        H += -p[i]*log2(p[i])

print('H(X) = ', H)
plt.show()






