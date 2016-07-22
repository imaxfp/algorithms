package sort

import scala.annotation.tailrec

/**
  * Created by Maxim.
  *
  * Selection Sort [Best/Worst: O(N^2)]
  *
  * 1. Scan all items and find the smallest
  * 2. Swap it into position as the first item.
  * 3. Repeat the selection sort on the remaining N-1 items.
  *
  **/
object SelectionSort {

  def sort(list: List[Int]): List[Int] = {
    selection(list)
  }

  @tailrec
  private def selection(arr: List[Int], res: List[Int] = List()): List[Int] = {
    if (arr.isEmpty) res
    else {
      val min = arr.indexOf(arr.min)
      selection(arr.filter(_ != min), res ++ List(min))
    }
  }
}
