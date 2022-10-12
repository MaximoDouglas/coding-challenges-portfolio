# https://www.codewars.com/kata/5839edaa6754d6fec10000a2

def get_alpha()
    ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  end
  
  def find_missing_letter(arr)
    alpha       = get_alpha()
    begin_index = alpha.index(arr[0].downcase)
    is_up_case  = arr[0] == arr[0].upcase
    missing     = nil
  
    arr.each_with_index do |item, index|
      alpha_index = begin_index + index
      if item.downcase != alpha[alpha_index]
        missing = is_up_case ? alpha[alpha_index].upcase : alpha[alpha_index]
        break
      end
    end
    
    missing
end
