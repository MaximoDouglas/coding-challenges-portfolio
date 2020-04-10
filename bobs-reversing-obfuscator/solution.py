def revert(string):
    reverted = ''
    for i in range(len(string) - 1, -1, -1):
        reverted += string[i]
        
    return reverted

def decoder(encoded, marker):
    encoded = encoded.replace(marker, '-')
    normal = []
    inverted = []
    indices = []
    
    for i, l in enumerate(encoded):
        if (l == '-'):
            indices.append(i)
    
    indices_size = len(indices)
    
    if (indices_size == 0):
        return encoded
    elif (indices_size == 1):
        return encoded[:indices[0]] + revert(encoded[indices[0] + 1:len(encoded)])
    else:
        
        for i in range(indices_size):
            if i%2 != 0:
                inverted.insert(0, revert(encoded[indices[i-1] + 1:indices[i]]))
                
                if (i + 1 == indices_size and indices[i] + 1 < len(encoded)):
                    normal.append(encoded[indices[i] + 1:])
            else:
                if (i - 1 >= 0):
                    normal.append(encoded[indices[i-1] + 1:indices[i]])
                else:
                    normal.append(encoded[:indices[i]])
                if(i + 1 == indices_size):
                    inverted.insert(0, revert(encoded[indices[i] + 1:len(encoded)]))
        
        string = ''
        for l in normal:
            string += l
        
        for l in inverted:
            string += l
        
        return string