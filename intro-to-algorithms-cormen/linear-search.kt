private val listOfIntegers = mutableListOf(5, 2, 4, 6, 1, 3)

private fun linearSearch(element: Int, list: MutableList<Int>): Int? {
    val n = list.size

    for (i in 0 until n) {
        if (list[i] == element) {
            return i
        }
    }

    return null
}

fun main() {
    println(linearSearch(7, listOfIntegers))
}
