import re

def solve(string):
  splitted = re.compile("[aeiou]").split(string)
  biggest = None

  str_numb = []
  for sequence in splitted:
    sumT = 0
    for char in sequence:
      sumT += ord(char) - 96
    
    if(biggest == None or sumT > biggest):
      biggest = sumT

  return biggest