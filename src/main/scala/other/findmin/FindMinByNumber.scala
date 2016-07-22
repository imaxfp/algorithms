package other.findmin

import scala.annotation.tailrec

/**
  * Created by Maxim.
  *
  * Find min element in the array by element number
  *
  * for example:
  *
  * arr == 3 4 5 8 10
  * fing == 3
  * res == 5
  * explanation
  * 1 - 3
  * 2 - 4
  * 3 - 5
  * Min 3 element will be 5
  *
  */
object FindMinByNumber {

  def processRecursion(arrUpdate: Array[Int], arrQuery: Array[Int]): Array[Int] = recursion(arrUpdate, arrQuery, 0, Array[Int]())

  /**
    * Algorithm complexity:
    * update  = [Best: O(N lg N), Avg: O(N lg N), Worst:O(N^2)]
    * query = O(1)
    *
    *
    * @param arrUpdate
    * @param arrQuery
    * @param n
    */
  @tailrec
  private def recursion(arrUpdate: Array[Int], arrQuery: Array[Int], n: Int, res: Array[Int]): Array[Int] = {
    if (n > arrUpdate.length - 1) return res
    val update = arrUpdate.take(n + 1).sortWith(_ < _)
    val query = arrQuery.apply(n)
    val nextMin = update.apply(query - 1)
    recursion(arrUpdate, arrQuery, n + 1, res ++ Array(nextMin))
  }

  /**
    * Algorithm complexity:
    *
    * update  = [Best: O(N lg N), Avg: O(N lg N), Worst:O(N^2)]
    * query = O(1)
    * @param arrUpdate
    * @param arrQuery
    * @return
    */
  def processIterative(arrUpdate: Array[Int], arrQuery: Array[Int]): Array[Int] = {
    var arr = Array[Int]()
    for (i <- arrUpdate.indices) {
      val update = arrUpdate.take(i + 1).sortWith(_ < _)
      val query = arrQuery.apply(i)
      arr = arr ++ Array(update.apply(query - 1))
    }
    arr
  }

  def processLiner(arrUpdate: Array[Int], arrQuery: Array[Int]) = {
    var arr = Array[Int]()
    for (i <- arrUpdate.indices) {
      val update = arrUpdate.take(i + 1)
      val query = arrQuery.apply(i)
      arr = arr ++ Array(minByPosition(update, query))
    }
    arr
  }

  /**
    * Algorithm complexity:
    *
    * [Best: O(N), Worst:O(N^2)]
    * @param arr
    * @param count
    * @return
    */
  @tailrec
  private def minByPosition(arr: Array[Int], count: Int): Int = {
    if (count == 1) return arr.min
    minByPosition(arr.filter(_ != arr.min), count - 1)
  }

}
