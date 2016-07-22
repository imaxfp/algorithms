package sort

import org.scalatest.FunSuite

/**
  * Created by Maxim.
  */
class SelectionSort$Test extends FunSuite {

  test("testSort") {
    val r = SelectionSort.sort(List(10, 9, 8, 7, 88, 6, 5, 4, 3, 2, 1))
    r.foreach(e => print(e + " "))
  }

}
