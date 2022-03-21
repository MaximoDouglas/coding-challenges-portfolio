# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3

def clean_string(s):
  new_string = ''
  b_count = 0
  for c in s[::-1]:
    if (c == '#'):
      b_count += 1
    elif (b_count == 0):
      new_string = c + new_string
    else:
      b_count -= 1
  
  return new_string