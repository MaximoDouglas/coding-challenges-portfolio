# https://www.codewars.com/kata/5544c7a5cb454edb3c000047

def bouncingBall(h, bounce, window):
    if (h <= 0 or bounce <= 0 or bounce >= 1 or window >= h):
        return -1
    
    counter = 1
    h = bounce*h
    while (h > window):
        counter += 2
        h = bounce*h
    
    return counter