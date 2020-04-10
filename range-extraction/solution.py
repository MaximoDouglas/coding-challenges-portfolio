def solution(args):
    begin = None
    end   = None
    
    string = ''
    for i, n in enumerate(args):
        if (begin == None):
            begin = n
            end   = n
            continue
        
        if (args[i - 1] + 1 == n):
            end = n
            if (i + 1 == len(args) and end - begin > 1):
                string += str(begin) + '-' + str(end)
            elif(i + 1 == len(args)):
                string += str(begin) + ',' + str(end)
        else:
            if (begin != end):
                if (end - begin > 1):
                    string += str(begin) + '-' + str(end)
                else:
                    string += str(begin) + ',' + str(end)
            else:
                string += str(end)
                
            if (i + 1 != len(args)):
                string += ','
            else:
                string += ',' + str(n)
            
            begin = n
            end   = n
    
    return string