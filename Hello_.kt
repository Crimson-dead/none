/**
 * You can edit, run, and share this code.
 * play.kotlinlang.org
 */
fun cube_of(num: Long) {
    print(num * num * num) // i had problem with return
}// */
fun main() {
    val name = "Frank"
    var num = 3 // Kotlin let's go!!
    println("Hello, $name! Square of $num is ${num * num}.")
    println("Cube of three is… (using function) ")
    cube_of(3)
    print("! ") // like in python
}
