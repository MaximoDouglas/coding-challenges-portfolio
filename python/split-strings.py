# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    l = []
    if (len(s) == 0):
        return []
        
    last = s[0]
    for i, c in enumerate(s):
        if (i%2 != 0):
            l.append(last + c)
        else:
            last = c
            if (i + 1 == len(s)):
                l.append(last + '_')
    return l
