# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string

def is_pangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True
