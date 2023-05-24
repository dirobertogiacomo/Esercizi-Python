import random
import string

codII = {'A': '1',
         'B': '01',
         'C': '001',
         'D': '000'}

fixed_length_code = {'A': '00',
                     'B': '01',
                     'C': '10',
                     'D': '11'}


def source_encoder(message:str):
    """
    Source encoder for codII.

    Giacomo Di Roberto, May 2023, version 1.0

    """

    coded_message = message
    for i in codII:
        coded_message = coded_message.replace(i,codII[i])
    
    return coded_message

def fixed_length_source_encoder(message:str):
    """
    Source encoder for fixed length code.

    Giacomo Di Roberto, May 2023, version 1.0

    """

    coded_message = message
    for i in fixed_length_code:
        coded_message = coded_message.replace(i,fixed_length_code[i])
    
    return coded_message

def source_decoder(coded_message):
    """
    Source decoder for codII.

    Giacomo Di Roberto, May 2023, version 1.0

    """
    
    message = coded_message
    for i in reversed(list(codII.keys())):
        message = message.replace(codII[i], i)
    
    return message

def genSymbol():
    """
    Generates a source symbol accordind to codII statistic.

    Giacomo Di Roberto, May 2023, version 1.0

    """

    p = random.random()

    if p >= 0.5:
        return 'A'
    
    if (p >= 0.25 and p < 0.5):
        return 'B'
    
    if p < 0.125:
        return 'D'
    else:
        return 'C'
    

N = 500
source_input = ''
encoder_output = ''
decoder_output = ''
fixed_length_encoder_output = ''

for i in range(N):

    # symbol generation
    s = genSymbol()
    source_input += s
    # coding (codII)
    c = source_encoder(s)
    encoder_output += c
    # coding (fixed length code)
    c = fixed_length_source_encoder(s)
    fixed_length_encoder_output += c
    # decding (codII)
    d = source_decoder(c)
    decoder_output += d

print('Input: ', source_input)
if decoder_output == source_input:
    print('Successfully decoded!')

print('Length of the code whith cod_II: ', len(encoder_output))
print('Length of the code whith fixed length code: ', len(fixed_length_encoder_output))
   