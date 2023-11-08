// https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

fun rotLeft(a: Array<Int>, d: Int): Array<Int> {
    val valuesOutOfBound = mutableListOf<Int>()

    a.forEachIndexed { index, value ->
        if (index + 1 <= d) {
            valuesOutOfBound.add(value)
        } else {
            a[index - d] = value
        }
    }
    
    var initIndex = a.size - valuesOutOfBound.size
    
    valuesOutOfBound.forEach {
        a[initIndex] = it
        initIndex++
     }
    
    return a
}
