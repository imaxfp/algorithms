package sort

import org.scalatest.FunSuite

/**
  * Created by Maxim.
  */
class InsertionSort$Test extends FunSuite {

  test("testSort") {
    val r = InsertionSort.sort(List(10, 9, 8, 7, 88, 6, 5, 4, 3, 2, 1))
    r.foreach(e => print(e + " "))
    println()

    val r2  = InsertionSort.sort(Array(10, 9, 8, 7, 88, 6, 5, 4, 3, 2, 1))
    r2.foreach(e => print(e + " "))
  }

}
