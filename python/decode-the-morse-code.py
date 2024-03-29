# https://www.codewars.com/kata/54b724efac3d5402db00065e

def decodeMorse(morse_code):
    words = morse_code.split('   ')
    
    returnPhrase = ''
    for word in words:        
        returnPhrase += ''.join(MORSE_CODE[letter] for letter in word.split()) + ' '
            
    return returnPhrase[:-1].lstrip()