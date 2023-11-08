import java.util.LinkedList

private val a = mutableListOf(1, 0, 1, 0, 1, 0, 1, 0)
private val b = mutableListOf(1, 1, 0, 0, 1, 1, 0, 0)

private fun binarySum(a: List<Int>, b: List<Int>): List<Int> {
    val n = a.size
    val result = LinkedList<Int>()
    var carry = 0

    for (i in (n - 1) downTo 0) {
        val sum = a[i] + b[i] + carry
        
        if (sum > 1) {
            carry = 1
            result.addFirst(0)
        } else {
            carry = 0
            result.addFirst(sum)
        }
    }

    if (carry != 0) {
        result.addFirst(carry)
    }
    
    return result
}

fun main() {
    println(binarySum(a, b))
}
