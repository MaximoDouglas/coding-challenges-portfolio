def divisors(n)
  list_div = []
  index    = 2
  
  while (index < n) do
    if (n%index == 0) then
      list_div.push(index)
    end
    
    index += 1
  end
  
  if (list_div.length == 0) then
    return "#{n} is prime"
  end
  
  return list_div
end
