# https://www.codewars.com/kata/550f22f4d758534c1100025a

def areOpposite(dir1, dir2):
    bool1 = (dir1 == 'NORTH' and dir2 == 'SOUTH') or (dir1 == 'SOUTH' and dir2 == 'NORTH')
    bool2 = (dir1 == 'EAST' and dir2 == 'WEST') or (dir1 == 'WEST' and dir2 == 'EAST') 
    return bool1 or bool2

def dirReduc(arr):
    oposites = []
    i = 0
    while i < len(arr) - 1:
        if (areOpposite(arr[i], arr[i+1])):
            oposites.append(i)
            oposites.append(i+1)
            i += 2
        else:
            i += 1
    
    if (len(oposites) == 0):
        return arr
    else:
        oposites.sort(reverse=True)
        for item in oposites:
            arr.pop(item)
            
        return dirReduc(arr)
