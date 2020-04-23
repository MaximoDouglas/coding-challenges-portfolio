def comp(array1, array2):
    if (array2 == None or array1 == None):
        return False
    
    size2 = len(array2)
    size1 = len(array1)
    
    if (size1 != size2):
        return False  
    
    for element in array1:
        sqr = element**2
        if (sqr in array2):
            array2.remove(sqr)
    
    return len(array2) == 0