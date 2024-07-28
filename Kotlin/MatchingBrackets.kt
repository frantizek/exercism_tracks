
fun isValid(input: String): Boolean {
    if (input.isEmpty()) {
        return true 
    }
    val messageBuilder = StringBuilder() 
    for (letra in input) {
    	when (letra.toString()) {
            "[" -> messageBuilder.append("[")
            "{" -> messageBuilder.append("{")
            "(" -> messageBuilder.append("(")
            "]" -> {
                    if (messageBuilder.toString().isEmpty()) {
	                    return false 
                    } else if (messageBuilder.last().toString() == "[") {
                        val lastIndex = messageBuilder.lastIndex 
                        if (lastIndex >= 0) {
                        	messageBuilder.deleteCharAt(lastIndex) 
                        }
                    } else {
                        return false
                    }
					// messageBuilder.append("]")
            }
            "}" -> {
                    if (messageBuilder.toString().isEmpty()) {
	                    return false 
                    } else if (messageBuilder.last().toString() == "{") {
                        val lastIndex = messageBuilder.lastIndex 
                        if (lastIndex >= 0) {
                        	messageBuilder.deleteCharAt(lastIndex) 
                        }
                    } else {
                        return false
                    }
					// messageBuilder.append("}")
            }
            ")" -> {
                    if (messageBuilder.toString().isEmpty()) {
	                    return false 
                    } else if (messageBuilder.last().toString() == "(") {
                        val lastIndex = messageBuilder.lastIndex 
                        if (lastIndex >= 0) {
                        	messageBuilder.deleteCharAt(lastIndex) 
                        }
                    } else {
                        return false
                    }
					// messageBuilder.append(")")            
            }
            else -> messageBuilder.append("")
        }
    }
    if (messageBuilder.toString().isEmpty()){
        return true
    }
    return false
}


fun main() {

    println(isValid(""))
    
}