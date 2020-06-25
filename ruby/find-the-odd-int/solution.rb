def find_it(seq)
    counter = {}
    
    seq.each { |n|
      counter[n] = counter[n] ? counter[n] += 1 : counter[n] = 1
    }
  
    counter.keys.each { |key|
      if (counter[key].remainder(2) != 0)
        return key
      end
    }
end