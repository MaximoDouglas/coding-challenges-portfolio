# https://www.codewars.com/kata/53368a47e38700bd8300030d

def list(names)
    list_size     = names.length
    string_return = ""
    
    names.each_with_index { |h, index|
      if (index > 0)
        string_return << (index == list_size - 1 ? " & " : ", ")
      end
      
      string_return << names[index][:name]
    }
    
    return string_return
end
