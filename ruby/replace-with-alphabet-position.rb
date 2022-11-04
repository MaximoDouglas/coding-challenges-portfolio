# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text)
    indexes = ('a'..'z').each_with_index.map{|l,i| [l, i+1]}.to_h
    
    string_return = ""
    letters = text.split('')
  
    letters.each_with_index{ |c, index|
      position = indexes[c.downcase]
  
      if position
        if string_return.length > 0 and index < letters.length
          string_return << " "
        end
  
        string_return << position.to_s
      end
    }
    
    return string_return
end
