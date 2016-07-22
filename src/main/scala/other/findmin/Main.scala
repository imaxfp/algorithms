package other.findmin

import scala.annotation.tailrec

/**
  * Created by Maxim.
  */
object Main {

  def main(args: Array[String]) {
    val sc = new java.util.Scanner(System.in)
    val size = sc.nextInt()
    val arr_update = init(size, Array[Int](), sc)
    val arr_query = init(size, Array[Int](), sc)


    print("array for update => ")
    arr_update.foreach(e => print(e + " "))
    println()
    print("array for queries => ")
    arr_query.foreach(e => print(e + " "))
  }

  @tailrec
  def init(n: Int, res: Array[Int], sc: java.util.Scanner): Array[Int] = {
    if (n == 0) return res
    init(n - 1, res ++ Array(sc.nextInt()), sc)
  }

}
