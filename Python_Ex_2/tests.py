import cryptoFunctions

text = open('Python_Ex_2/text.txt').read()

# Caecer Enc/Dec example of usage
shift = 5
cyphCaecer = cryptoFunctions.CaecerEnc(text, shift)
plainCaecer = cryptoFunctions.CaecerDec(cyphCaecer, shift)
print(plainCaecer == cryptoFunctions.textConverter(text))


# Vigenere Enc/Dec example of usage
key = 'GKDRI'
cyphVigenere = cryptoFunctions.VigenereEnc(text, key)
plainVigenere = cryptoFunctions.VigenereDec(cyphVigenere, key)
print(plainVigenere == cryptoFunctions.textConverter(text))

