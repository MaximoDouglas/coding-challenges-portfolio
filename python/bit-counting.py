# https://www.codewars.com/kata/526571aae218b8ee490006f4

def countBits(n):
    sum = 0
    while (n >= 1):
        r = n%2
        if (r == 1):
            sum += 1
        n = n//2
    
    return sum