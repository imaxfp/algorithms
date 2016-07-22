package other

import scala.annotation.tailrec

/**
  * Created by Maxim.
  */
object MergeLists {

  /**
    * merge list algorithm.
    * Each of list sorted from min to max
    *
    * Example:
    * ListA = 1 2 4 6 100
    * ListB = 5
    * ListRes = 1 2 4 5 6 100
    *
    * @param a
    * @param b
    * @param res
    * @return
    */
  @tailrec
  def mergeList(a: List[Int], b: List[Int], res: List[Int]): List[Int] = {
    if (a.isEmpty) return res ::: b
    if (b.isEmpty) return res ::: a
    if (a.head < b.head) mergeList(a.tail, b, res ::: List(a.head)) else
    mergeList(a, b.tail, res ::: List(b.head))
  }


}
