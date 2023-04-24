
codII = {'A': '1',
         'B': '01',
         'C': '001',
         'D': '000'}

def source_encoder(message:str):

    coded_message = message
    for i in codII:
        coded_message = coded_message.replace(i,codII[i])
    
    return coded_message

def source_decoder(coded_message):
    
    message = coded_message
    for i in reversed(list(codII.keys())):
        message = message.replace(codII[i], i)
    
    return message

txt = 'ABCDBDCABDCAACDBACDDBDC'
coded = source_encoder(txt)
encoded = source_decoder(coded)
print(coded)
print(encoded)
if encoded == txt :
    print('Successfully decoded!')

        
    