import freqAnalysis
import matplotlib.pyplot as plt
import pandas as pd


text = open('Python_Ex_1/text.txt').read()

freqData = freqAnalysis.freqAnalysis(text)
freqData = pd.DataFrame(freqData)
freqData_sorted = freqData.sort_values('Frequence', ascending=False)


# plotting the results 
plt.figure()
plt.bar('Letter', 'Frequence', data=freqData) # alphabetic order
plt.ylabel('Frequence (%)')
plt.figure()
plt.bar('Letter', 'Frequence', data=freqData_sorted) # sorted by frequency
plt.ylabel('Frequence (%)')
plt.show()


