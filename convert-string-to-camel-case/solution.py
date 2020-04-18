def to_camel_case(text):
    splittedString = text.replace('_', '-').split('-')
    
    phrase = ''
    for i, word in enumerate(splittedString):
        if (i == 0):
            phrase += word
        else:
            phrase += word[0].upper() + word[1:]
    
    return phrase