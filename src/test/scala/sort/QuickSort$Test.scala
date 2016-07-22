package sort

import org.scalatest.FunSuite

/**
  * Created by Maxim.
  */
class QuickSort$Test extends FunSuite {

  val arr = Array(4, 1, 2, 7, 88)

  test("testSort") {
    val r = QuickSort.sort(arr)
    r.foreach(e => print(e + " "))
  }

}
