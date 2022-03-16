// https://www.hackerrank.com/challenges/sock-merchant/problem

fun sockMerchant(n: Int, ar: Array<Int>): Int {
    var colorsMap = HashMap<Int, Int> ()
    
    ar.forEach { color ->
        val alreadyInMap = colorsMap.getOrDefault(color, 0)
        colorsMap.put(color, alreadyInMap + 1)
    }
    
    var amountOfPairs = 0
    
    colorsMap.forEach { _, amount ->
        amountOfPairs += ((amount - amount%2)/2).toInt()
    }

    return amountOfPairs
}