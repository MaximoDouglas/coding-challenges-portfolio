def pig_it(text):
    splitted_string = text.split()
    
    phrase = ''
    for i, word in enumerate(splitted_string):
        if (word.isalpha()):
            phrase += word[1:] + word[0] + 'ay'
        else:
            phrase += word
            
        if (i + 1 < len(splitted_string)):
            phrase += ' '
            
    return phrase