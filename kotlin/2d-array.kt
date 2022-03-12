// https://www.hackerrank.com/challenges/2d-array/

fun hourglassSum(arr: Array<Array<Int>>): Int {
    val lastIndexToSearch = 3
    var biggestSum = Int.MIN_VALUE
    
    for (row in 0..lastIndexToSearch) {
        for (column in 0..lastIndexToSearch) {
            val sumRowOne = arr[row].copyOfRange(column, column + 3).sum()
            val sumRowTwo = arr[row+1][column+1]
            val sumRowThree = arr[row+2].copyOfRange(column, column + 3).sum()
            
            val totalHourglassSum = sumRowOne + sumRowTwo + sumRowThree
            
            if (totalHourglassSum > biggestSum) {
                biggestSum = totalHourglassSum
            }
        }
    }
    
    return biggestSum
}