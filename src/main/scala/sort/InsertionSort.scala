package sort

import scala.annotation.tailrec
import scala.util.control.Breaks

/**
  * Created by Maxim.
  *
  * Insertion Sort [Best: O(N), Worst:O(N^2)]
  *
  * 1. Start with a sorted list of 1 element on the left.
  * 2. N-1 unsorted items on the right.
  * 3. Take the first unsorted item (element #2) and INSERT it into the sorted list, moving elements as necessary.
  * 4. Repeat the selection sort on the remaining N-1 items.
  *
  **/

object InsertionSort {

  def sort(list: List[Int]): List[Int] = {
    insertionRec(list, List())
  }

  @tailrec
  private def insertionRec(list: List[Int], res: List[Int]): List[Int] = {
    if (list.isEmpty) return res
    val res2 = res.partition(_ <= list.head)
    insertionRec(list.tail, res2._1 ::: List(list.head) ::: res2._2)
  }

  val loop = new Breaks

  def sort(arr: Array[Int]): Array[Int] = {
    for (i <- arr.indices) {
      var tmp = arr.apply(i)
      loop.breakable {
        for (j <- i to 1 by -1) {
          if (arr.apply(j - 1) <= tmp) loop.break
          tmp = arr.apply(j)
          arr.update(j, arr.apply(j - 1))
          arr.update(j - 1, tmp)
        }
      }
    }
    arr
  }

}
