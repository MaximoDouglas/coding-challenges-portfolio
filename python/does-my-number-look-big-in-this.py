# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic( value ):
    strNumber  = str(value)
    digits_len = len(strNumber)
    
    sum = 0
    for digit in strNumber:
        sum += int(digit)**(digits_len)
        
    return value == sum
