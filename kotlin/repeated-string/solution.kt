// https://www.hackerrank.com/challenges/repeated-string/problem

fun repeatedString(s: String, n: Long): Long {
    var aCounter = 0L
    var index = 0
    var remainderCounter = 0
    
    var stringLength = s.length
    var maxIntegerRepetitions = n/stringLength
    var remainderLength = n - (stringLength * maxIntegerRepetitions)
    
    for (i in 0 until stringLength) {
        if (s.get(index) == 'a') {
             aCounter += 1
         
             if (index < remainderLength) {
                 remainderCounter += 1
             }
        }
        
        index += 1
    }
    
    return (aCounter * maxIntegerRepetitions) + remainderCounter
}