import math

def rec(arr, begin, end):
    if (begin == end):
        if (arr[begin] == begin):
            return begin
        else:
            return -1
    
    pivot = math.floor((end + begin)/2)
    if (arr[pivot] < 0 or arr[pivot] < pivot):
        return rec(arr, pivot + 1, end)
    elif (arr[pivot] > pivot):
        return rec(arr, begin, pivot - 1)
    elif (arr[pivot] == pivot):
        return rec(arr, begin, pivot)

def index_equals_value(arr):
    sz = len(arr)
    pivot = math.floor(sz/2)
    if (arr[pivot] < 0 or arr[pivot] < pivot):
        return rec(arr, pivot + 1, sz - 1)
    elif (arr[pivot] > pivot):
        return rec(arr, 0, pivot - 1)
    elif (arr[pivot] == pivot):
        return rec(arr, 0, pivot)
        
    return -1