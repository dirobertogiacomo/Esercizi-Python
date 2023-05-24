import cryptoFunctions as crf
from math import log2

text = crf.textConverter(open('Python_Ex_8/text_it.txt').read(), space=False)

# frequency analysis
freq = crf.blocksFreqAnalysis(text)

# computing the entropy 
H = 0
for i in range(len(freq)):
    if freq[i]:
        H += -(freq[i]/100)*log2((freq[i]/100))

print('H(X1, X2) = ', H/2)

# check if the sum of relative frequencies is 1
print('Sum of relative frequencies: ',sum(freq)/100)
