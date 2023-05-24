import cryptoFunctions

text = open('Python_Ex_2/text.txt').read()

# Caecer Enc/Dec example of usage

shift = 5
# coding
ciphCaecer = cryptoFunctions.CaecerEnc(text, shift)
# writing the encoded text to an external file
f = open('Python_Ex_2/Caecer_coding.txt', 'w').write(ciphCaecer)
# decoding
plainCaecer = cryptoFunctions.CaecerDec(ciphCaecer, shift)

print(plainCaecer == cryptoFunctions.textConverter(text))


# Vigenere Enc/Dec example of usage

key = 'GKDRI'
# coding
ciphVigenere = cryptoFunctions.VigenereEnc(text, key)
# writing the encoded text to an external file
f = open('Python_Ex_2/Vigenere_coding.txt', 'w').write(ciphVigenere)
# decoding
plainVigenere = cryptoFunctions.VigenereDec(ciphVigenere, key)

print(plainVigenere == cryptoFunctions.textConverter(text))

