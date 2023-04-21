import string
from unidecode import unidecode

def textConverter(text, space = False):
    """
    This funcion return the input string whitout puntuaction, numbers and whitespaces and
    where all characters are in upper case.
    If the argument 'space' is True, the whitespaces are not removed.  
    
    Giacomo Di Roberto, March 2023, version 1.2 

    """

    # decoding special characters such as accented characters 
    text = unidecode(text)
    # converting the string in upper case
    text = text.upper()
    # deleting punctuation 
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits))
    # deleting white spaces, returns, tabs, etc... 
    if (not space):
        text = text.translate( {ord(c) : '' for c in string.whitespace} )

    return text

def freqAnalysis(text, space = False):
    """
    This function perform a frequency analysis of the given text.
    If the argument 'space' is True, the space character is also included in the analysis.

    Giacomo Di Roberto, March 2023, version 1.1

    """ 

    # list of alphabet letters and space
    alph = ["A", "B","C","D","E","F","G","H","I",
            "J","K","L","M","N","O","P","Q","R",
            "S","T","U","V","W","X","Y","Z","space"]

    L = len(text)

    # computing the frequencies for each character (in %)
    freq = [None]*26
    for i in range(26):
        freq[i] = text.count(string.ascii_uppercase[i])/L*100
    
    # computing the frequence of the space, if required (in %)
    if space:
        space_freq = 0
        for i in range(len(string.whitespace)):
            space_freq += (text.count(string.whitespace[i])/L*100)
        freq.append(space_freq)
    else:
        alph.remove("space")

    freqData = {'Frequence' : freq,
                'Letter' : alph}
    
    return freqData
