def DNA_strand(dna)
  chars = dna.split('')
  
  complements   = {"A": "T", "T": "A", "C": "G", "G": "C"}
  return_string = ""
  
  chars.each { |c|
      return_string << complements[c.to_sym]
  }
  
  return_string
end