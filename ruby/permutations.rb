# https://www.codewars.com/kata/5254ca2719453dcc0b00027d

def permutations(string)
    string.chars.permutation.map(&:join).uniq()
end
