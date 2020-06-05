def generate_hashtag(s):
    splitted = s.split()
    
    if (len(s) == 0 or len(s) > 140):
        return False
    
    phrase = '#'
    for w in splitted:
        phrase += w[0].upper() + w[1:].lower()
    
    if (phrase == '#'):
        return False
        
    return phrase