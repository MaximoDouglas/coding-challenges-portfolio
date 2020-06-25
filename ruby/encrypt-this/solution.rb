def encrypt_this(text)
    words  = text.split(' ')
    phrase = ""
    
    words.each_with_index { |word, index|
      if (index > 0)
        phrase << " "
      end
      
      letters     = swap_letters(word.chars)
      first_ascii = letters[0].sum.to_s
      
      phrase << build_word(first_ascii, letters)
    }
    
    return phrase
  end
  
  def swap_letters(letters)
    size = letters.length
    
    if (size > 1)
      letters[size - 1], letters[1] = letters[1], letters[size - 1]
    end
    
    return letters
  end
  
  def build_word(first_ascii, letters)
    word = first_ascii
    
    letters.each_with_index { |letter, index|
      if (index > 0)
        word << letter
      end
    }
    
    return word
end