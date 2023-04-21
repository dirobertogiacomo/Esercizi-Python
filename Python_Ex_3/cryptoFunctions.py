import string
from unidecode import unidecode

def textConverter(text):
    """
    This funcion return a string whitout puntuaction, numbers and whitespaces and
    where all characters are in upper case 
    
    Giacomo Di Roberto, March 2023, version 1.1 

    """

    # decoding special characters such as accented characters 
    text = unidecode(text)
    # converting the string in upper case
    text = text.upper()
    # deleting punctuation 
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits))
    # deleting white spaces, returns, tabs, etc... 
    text = text.translate( {ord(c) : '' for c in string.whitespace} )

    return text


def CaecerEnc(text, shift):
    """
    This function perform a Caecer's encryption of the given text

    Giacomo Di Roberto, March 2023, version 1.1 

    """

    text = textConverter(text)
    shift = shift%26

    # computing shifted alphabet
    sht_alph = (string.ascii_uppercase + string.ascii_uppercase)[shift:26+shift]
    
    # replacing normal alphabet with shifted alphabet 
    text = text.translate(str.maketrans(string.ascii_uppercase, sht_alph))
    
    return text

def CaecerDec(text, shift):
    """
    This function perform a Caecer's decryption of the given text.

    Giacomo Di Roberto, March 2023, version 1.1 
    
    """

    shift = shift%26

    # computing shifted alphabet
    sht_alph = (string.ascii_uppercase + string.ascii_uppercase)[shift:26+shift]

    # replacing the alphabet 
    text = text.translate(str.maketrans(sht_alph, string.ascii_uppercase))

    return text

def VigenereEnc(text, key):
    """
    This function perform a Vigenere's encryption of the given text, according
    to the given key. The key must be an upper case string. 

    Giacomo Di Roberto, March 2023, version 1.0 
    
    """

    text = textConverter(text)

    # constants
    C = len(key) # number of alphabets 
    L = len(text) # length of the text
    shift = [0]*C 
    for i in range(C): shift[i] = ord(key[i])-ord('A') # number of shifts for every alphabets

    # dividing the text in C strings

    div_text = ['']*C
    div_text_len = [0]*C

    for i in range(C):
        div_text[i] = text[i::C] # taking one character every C characters
    
    # encoding each string 

    for i in range(C):
        div_text[i] = CaecerEnc(div_text[i], shift[i])
        div_text_len[i] = len(div_text[i])
    

    # rebuilding the cyphered text in one sting 
    
    Lmin = min(div_text_len) # minimum length of the strings
    Lmax = max(div_text_len) # maximum length of the strings
    cyph_text = ''
    tmp_str = ''

    for i in range(Lmin):
        for j in range(C):
            tmp_str = tmp_str + div_text[j][i]
        cyph_text = cyph_text + tmp_str
        tmp_str = ''

    # if any of the C strings are longer than the others

    if len(cyph_text) != L:
        j = L - len(cyph_text)
        for i in range(j):
            tmp_str = tmp_str + div_text[i][Lmax-1]
        cyph_text = cyph_text + tmp_str
        tmp_str = ''

    return cyph_text

def VigenereDec(text, key):
    """
    This function perform a Vigenere's decryption of the given text, according
    to the given key. The key must be an upper case string. 

    Giacomo Di Roberto, March 2023, version 1.0 
    
    """

    # constants
    C = len(key) # number of alphabets 
    L = len(text) # length of the text
    shift = [0]*C 
    for i in range(C): shift[i] = abs(ord(key[i])-ord('A')) # number of shifts for every alphabets

    # dividing the text in C strings

    div_text = ['']*C
    div_text_len = [0]*C

    for i in range(C):
        div_text[i] = text[i::C] # taking one character every C characters
    
    # decoding each string 

    for i in range(C):
        div_text[i] = CaecerDec(div_text[i], shift[i])
        div_text_len[i] = len(div_text[i])
    
    # rebuilding the plain text in one sting 
    
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

    return plain_text

def freqAnalysis(text):
    """
    This function perform a frequency analysis of the given text.

    Giacomo Di Roberto, March 2023, version 1.0

    """ 

    # list of alphabet letters
    alph = ["A", "B","C","D","E","F","G","H","I",
            "J","K","L","M","N","O","P","Q","R",
            "S","T","U","V","W","X","Y","Z"]

    text = textConverter(text)

    L = len(text)

    # computing the frequencies for each character (in %)
    freq = [None]*26
    for i in range(26):
        freq[i] = text.count(string.ascii_uppercase[i])/L*100

    freqData = {'Frequence' : freq,
                'Letter' : alph}
    
    return freqData
