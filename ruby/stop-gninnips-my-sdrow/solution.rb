def spinWords(string)
    string_to_return = ""
    
    string.split(' ').each_with_index { |word, index|
      w = index > 0 ? " " : ""
      
      if (word.length >= 5)
        w << word.reverse
      else
        w << word
      end
      
      string_to_return << w
    }
    
    string_to_return
end