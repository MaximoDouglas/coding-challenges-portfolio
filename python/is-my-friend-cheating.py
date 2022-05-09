# https://www.codewars.com/kata/5547cc7dcad755e480000004

def removNb(n):
    d = {}
    total = ((n+1)*n)/2
    
    for i in range(1, n+1):
        x = (total - i)/(1 + i)
        if (x > n):
            continue
        if (x != i and (round(x) - x) == 0):
            d[x] = i
            d[i] = x
    
    sorted_list = sorted(list(d))
    
    return_list = []
    for k in sorted_list:
        return_list.append((k, d[k]))
        
    return return_list
