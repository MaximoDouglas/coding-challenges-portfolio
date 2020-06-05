def unique_in_order(iterable)
    last        = nil
     return_list = []
     
     if iterable.class == "".class
         iterable = iterable.split('')
     end
       
     iterable.each{ |n|
       if n != last 
         return_list << n
       end
         
       last = n
     }
       
     return_list
end