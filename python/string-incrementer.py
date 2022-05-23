# https://www.codewars.com/kata/54a91a4883a7de5d7800009c

numbers = ['0', '1', '2', '3', '4',
          '5', '6', '7', '8', '9']

def increment_string(string):
    string_len = len(string)

    if (string_len == 0):
      return '1'

    last_index = string_len
    for i in range((string_len - 1), -1, -1):
        if (string[i] not in numbers):
            break
        else:
            last_index = i
    
    if (last_index == string_len):
        return string + '1'
    else:
        number = int(string[last_index:]) + 1
        nLen = len(string[last_index:])

        return string[:last_index] + str(number).zfill(nLen)
