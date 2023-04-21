from unidecode import unidecode
import string


def textConverter(text):
    """
    This funcion return a string whitout puntuaction and whitespacese and
    where all characters are in upper case. 
    
    Giacomo Di Roberto, March 2023, version 1.0 

    """

    # decoding special characters such as accented characters 
    text = unidecode(text)
    # converting the string in upper case
    text = text.upper()
    # deleting punctuation 
    text = text.translate(str.maketrans('', '', string.punctuation))
    # deleting white spaces, returns, tabs, etc... 
    text = text.translate( {ord(c) : '' for c in string.whitespace} )

    return text

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
