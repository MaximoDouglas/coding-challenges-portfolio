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