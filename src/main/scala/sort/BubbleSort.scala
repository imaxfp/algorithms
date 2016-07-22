package sort

/**
  * Created by Maxim.
  *
  * Bubble Sort [Best: O(n), Worst:O(N^2)]
  *
  * 1. Starting on the left, compare adjacent items and keep “bubbling” the larger one to the right
  * 2. N-1 right side after N+1 step
  *
  **/
object BubbleSort {


  def sort(arr: Array[Int]): Array[Int] = {
    var tmp = 0
    for (i <- arr.indices) {
      for (j <- 0 to arr.length - (i+2)) {
        if (arr.apply(j) > arr.apply(j + 1)) {
          tmp = arr.apply(j)
          arr.update(j, arr.apply(j + 1))
          arr.update(j + 1, tmp)
        }
      }
    }
    arr
  }

  //@tailrec
  private def sortRec(l: List[Int], res: List[Int]): List[Int] = {
    if (l.isEmpty) return res

    if (l.head > l.tail.head) {
      sortRec(l.tail.tail, res ++ List(l.tail.head) ++ List(l.head))
    } else {
      sortRec(l.tail.tail, res ++ List(l.head) ++ List(l.tail.head))
    }
  }

}
