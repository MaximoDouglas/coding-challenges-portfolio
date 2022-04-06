# https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    splittedString = text.replace('_', '-').split('-')
    
    phrase = ''
    for i, word in enumerate(splittedString):
        if (i == 0):
            phrase += word
        else:
            phrase += word[0].upper() + word[1:]
    
    return phrase