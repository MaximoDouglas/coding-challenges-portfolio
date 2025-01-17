// https://www.hackerrank.com/challenges/minimum-swaps-2/problem

fun minimumSwaps(arr: Array<Int>): Int {
    var swapAmount = 0
    var diffIndexes = arr.indices.toList()

    while (diffIndexes.isEmpty().not()) {
        val auxDiffIndexes = mutableListOf<Int>()

        for (i in diffIndexes) {
            if (arr[i] != i.inc()) {
                val aux = arr[arr[i].dec()]
                arr[arr[i].dec()] = arr[i]
                arr[i] = aux

                if (arr[i] != i.inc()) {
                    auxDiffIndexes.add(i)
                }

                swapAmount++
            }
        }

        diffIndexes = auxDiffIndexes
    }

    return swapAmount
}