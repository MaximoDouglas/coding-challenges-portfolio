// https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

fun jumpingOnClouds(c: Array<Int>): Int {
    val listSize = c.size
    var jumps = 0
    
    var i = 0
    while (i < listSize) {
        if (i + 2 < listSize && c[i+2] == 0) {
            jumps += 1
            i += 1
        } else if (i + 1 < listSize) {
            jumps += 1
        }
        
        i += 1
    }

    return jumps
}