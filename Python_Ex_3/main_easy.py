import cryptoFunctions as crf
import matplotlib.pyplot as plt
import pandas as pd

ciphr_text = crf.textConverter(open('Python_Ex_3/cipheredtext.txt').read())

# dividing the text in C strings
C = 6

freqData = [None]*C
div_text = ['']*C

fig, axs = plt.subplots(C)

for i in range(C):

    # taking one character every C characters
    div_text[i] = ciphr_text[i::C] 

    # frequency analysis for each string
    freqData[i] = pd.DataFrame(crf.freqAnalysis(div_text[i])).sort_values('Frequence', ascending=False) 
    axs[i].bar('Letter', 'Frequence', data=freqData[i])


key = 'ASIMOV'

# decripting the text with Vigenere's decoder
plain_text = crf.VigenereDec(ciphr_text, key)

# printing the first 200 characters
print(plain_text[:200]) 

# plot
fig.tight_layout()
plt.show()

# saving the deciphered text
decipheredtext = open("Python_Ex_3\decipheredtext.txt", "w").write(plain_text)
