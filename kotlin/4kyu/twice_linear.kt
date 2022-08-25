package dbllinear
fun dblLinear(n:Int):Int {
    val u : MutableList<Int> = mutableListOf(1)
    var x:Int = 0;
    var y:Int = 0;
    val fx = {j:Int -> 2*j + 1}
    val fy = {j:Int -> 3*j + 1}

    for (i in 1..n){
        var valx = fx(u[x])
        var valy = fy(u[y])
        if (valx <= valy){
            u.add(valx)
            x++
            if (valx == valy){
                y++
            }
        } else {
            u.add(valy)
            y++
        }
    }
    return u.last()
}
