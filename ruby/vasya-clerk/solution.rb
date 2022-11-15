# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8

def tickets(people)
    bills = { 25 => 0, 50 => 0, 100 => 0 }
    
    people.each { |n|
      if n == 25
        bills[25] += 1
      elsif n == 50
        if bills[25] >= 1
          bills[25] -= 1
        else
          return 'NO'
        end
        
        bills[50] += 1
      else
        if (bills[25] >= 1 and bills[50] >= 1)
          bills[25] -= 1
          bills[50] -= 1
          bills[100] += 1
        elsif (bills[25] >= 3)
          bills[25] -= 3
          bills[100] += 1
        else
          return 'NO'
        end
      end
    }
    
    return 'YES'
end
