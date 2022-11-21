# https://www.codewars.com/kata/5277c8a221e209d3f6000b56

def validBraces(braces)
    last_opened  = []
    
    braces.split('').each{ |c|
      if c == '('
        last_opened.push(c)
      elsif (c == ')')
        lo_size = last_opened.length
        if lo_size == 0 or last_opened[lo_size - 1] != '('
          return false
        else
          last_opened.pop
        end
      elsif c == '['
        last_opened.push(c)
      elsif (c == ']')
        lo_size = last_opened.length
        if lo_size == 0 or last_opened[lo_size - 1] != '['
          return false
        else
          last_opened.pop
        end
      elsif c == '{'
        last_opened.push(c)
      elsif (c == '}')
        lo_size = last_opened.length
        if lo_size == 0 or last_opened[lo_size - 1] != '{'
          return false
        else
          last_opened.pop
        end
      end
    }
  
    return last_opened.length == 0
end
