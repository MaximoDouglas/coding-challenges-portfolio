def digital_root(n):
    strNumber = str(n)
    
    sum = 0
    for d in strNumber:
        sum += int(d)
    
    if (len(str(sum)) > 1):
        return digital_root(sum)
    else:
        return sum