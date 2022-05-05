# https://www.codewars.com/kata/5679aa472b8f57fb8c000047

def find_even_index(arr):
    s = sum(arr)
    
    left = 0
    for i in range(len(arr)):
        right = s - left - arr[i]
        
        if (left == right):
            return i
            
        left += arr[i]
    
    return -1
