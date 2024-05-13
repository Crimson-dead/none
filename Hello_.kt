fun cubeOf(num: Long): Long { /* Now ik, the type of 
    *returned value must be defined
    */
    return num * num * num
}

fun main(args: Array<String>) {
    val name = "Someone"
    var num = 3 // Gotcha!
    println("Hello, ${args[0]}! Square of $num is ${num * num}.")
    println("Cube of three is… (using function) \n${cubeOf(3)}! ")
    print("\nCreated by $name. ") // like in python
}
