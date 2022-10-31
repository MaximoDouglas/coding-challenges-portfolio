# https://www.codewars.com/kata/55983863da40caa2c900004e

def only_repeated_digits(digits)
    any_digit = digits[0]
  
    digits.each { |n|
      if n != any_digit
        return false
      end
    }
  
    return true
  end
  
  def is_desc_order(digits)
    last_seen_number = digits[0]
  
    digits.each { |new_number|
      if (new_number > last_seen_number)
        return false
      end
  
      last_seen_number = new_number
    }
  
    return true
  end
  
  def is_same_digits(number_array_1, number_array_2)
    number_array_1.sort == number_array_2.sort
  end
  
  def map_number_to_array(number)
    return number.to_s.split('').map{|d| d.to_i}
  end
  
  def next_bigger(n)
    digits = map_number_to_array(n)
    
    if (digits.length == 1) or only_repeated_digits(digits) or is_desc_order(digits)
      return -1
    end
  
    target_number = n
    while true
      target_number       += 1
      target_number_array = map_number_to_array(target_number)
      
      if is_same_digits(digits, target_number_array)
        return target_number
      end
    end
end
