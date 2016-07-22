package sort

import org.scalatest.FunSuite

/**
  * Created by Maxim.
  */
class BubbleSort$Test extends FunSuite {

  test("Test iterative sorting") {
    val r = BubbleSort.sort(Array(10,9,8,7,88,6,5,4,3,2,1))
    r.foreach(e => print(e + " "))
  }

  test("Test iterative sorting") {
    val r = BubbleSort.sort(Array(10,9,8,7,88,6,5,4,3,2,1))
    r.foreach(e => print(e + " "))
  }


}
