object Raindrops {

    fun convert(n: Int): String {
    
        val Pli: String = "Pling"
        val Pla: String = "Plang"
        val Plo: String = "Plong"
        
        if (n % 3 == 0 && n % 5 == 0 && n % 7 == 0) {
            return Pli+Pla+Plo
        } else if (n % 3 == 0 && n % 5 == 0) {
            return Pli+Pla 
        } else if (n % 3 == 0 && n % 7 == 0) {
            return Pli+Plo 
        } else if (n % 5 == 0 && n % 7 == 0) {
            return Pla+Plo 
        } else if (n % 3 == 0) {
            return Pli
        } else if (n % 5 == 0) {
            return Pla
        } else if (n % 7 == 0) {
            return Plo
        } else {
            return n.toString()
        }
    }
}
