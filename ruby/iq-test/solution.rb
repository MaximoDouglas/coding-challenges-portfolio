def iq_test(numbers)
    even_list    = []
    odd_list     = []
    number_list  = numbers.split(' ')
  
    number_list.each_with_index do |item, index|
      if (item.to_i) % 2 == 0
        even_list.append(index)
      else
        odd_list.append(index)
      end
    end
  
    return (even_list.length < odd_list.length ? even_list[0] : odd_list[0]) + 1
end