def countBits(n):
    sum = 0
    while (n >= 1):
        r = n%2
        if (r == 1):
            sum += 1
        n = n//2
    
    return sum