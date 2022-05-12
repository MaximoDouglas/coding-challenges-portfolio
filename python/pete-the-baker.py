# https://www.codewars.com/kata/525c65e51bf619685c000059

import math

def cakes(recipe, available):
    minimun = None
    
    if len(recipe) > len(available):
        return 0
    
    for ing in recipe:
        if (ing not in available):
            return 0
        if (recipe[ing] > available[ing]):
            return 0
        total = available[ing]/recipe[ing]
        
        if (minimun == None or total < minimun):
            minimun = math.floor(total)
    
    return minimun
