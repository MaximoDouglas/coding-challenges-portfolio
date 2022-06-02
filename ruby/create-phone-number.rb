# https://www.codewars.com/kata/525f50e3b73515a6db000b83

def createPhoneNumber(numbers)
    return_string = ""
    numbers.each_with_index { |n, index|
      if (index == 0)
        return_string << ("(" + n.to_s)
      elsif (index == 2)
        return_string << (n.to_s + ") ")
      elsif (index == 5)
        return_string << (n.to_s + "-")
      else
        return_string << n.to_s
      end
    }
    
    return return_string
end
