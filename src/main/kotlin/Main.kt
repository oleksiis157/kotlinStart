import java.util.Scanner

fun main() {


    val scanner = Scanner(System.`in`)
    val min = scanner.nextInt()
    val hours = min / 60


    if (hours > 1) {
        println("$hours hours")
    } else {
        println("$hours hour")
    }
}
