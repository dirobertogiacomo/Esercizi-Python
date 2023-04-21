import cryptoFunctions as crf
import matplotlib.pyplot as plt
import pandas as pd

cyphr_text = crf.textConverter(open('Python_Ex_3\cipheredtextp.txt').read())

alph_it = ['EAOINRTLSCDUPMVGHBFQZYXKJW',
           'EAIONRTLSCDUPMVGHBFQZYXKJW',
           'EIAONRTLSCUDPMVGBHFQZYXKJW']


# dividing the text in C strings
C = 3

freqData = [None]*C
div_text = ['']*C
div_text_len = [None]*C
alph = ['']*C
key = ''

fig, axs = plt.subplots(C)


for i in range(C):

    # taking one character every C characters
    div_text[i] = cyphr_text[i::C]
    div_text_len[i] = len(div_text[i]) 

    # frequency analysis for each string
    freqData[i] = pd.DataFrame(crf.freqAnalysis(div_text[i])).sort_values('Frequence', ascending=False)
    # saving the permuted alphabets  
    alph[i] = crf.textConverter(freqData[i]['Letter'].to_string(header=False, index=False))
    # plot 
    axs[i].bar('Letter', 'Frequence', data=freqData[i])

# plot
fig.tight_layout()
plt.show()

# replacing the alphabets 
for i in range(C):
    div_text[i] = div_text[i].translate(str.maketrans(alph[i], alph_it[i]))

# rebuilding the plain text in one sting 

L = len(cyphr_text)
Lmin = min(div_text_len) # minimum length of the strings
Lmax = max(div_text_len) # maximum length of the strings
plain_text = ''
tmp_str = ''

for i in range(Lmin):
    for j in range(C):
        tmp_str = tmp_str + div_text[j][i]
    plain_text = plain_text + tmp_str
    tmp_str = ''

# if any of the C strings are longer than the others

if len(plain_text) != L:
    j = L - len(plain_text)
    for i in range(j):
        tmp_str = tmp_str + div_text[i][Lmax-1]
    plain_text = plain_text + tmp_str
    tmp_str = ''

# printing the first 200 characters 
print(plain_text[:200])

# saving the deciphered text
decipheredtext = open("Python_Ex_3\decipheredtextp.txt", "w").write(plain_text)

