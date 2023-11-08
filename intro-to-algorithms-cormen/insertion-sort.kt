val listOfIntegers = mutableListOf(5, 2, 4, 6, 1, 3)

fun insertionSort(list: MutableList<Int>): List<Int> {
    val n = list.size

    for (i in 1 until n) {
        val key = list[i]
        var j = i - 1

        while (j >= 0 && list[j] > key) {
            list[j+1] = list[j]
            j--
        }

        list[j+1] = key
    }

    return list
}

fun main() {
    println(insertionSort(listOfIntegers))
}