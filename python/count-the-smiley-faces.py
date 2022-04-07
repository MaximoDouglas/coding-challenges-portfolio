# https://www.codewars.com/kata/583203e6eb35d7980400002a

import re

def count_smileys(arr):
    counter = 0
    
    for s in arr:
        found = re.search('^[:;][-~]*[)D]', s)
        if (found != None):
            counter += 1
            
    return counter
