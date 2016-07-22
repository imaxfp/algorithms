package sort

/**
  * Created by Maxim.
  *
  * Quicksort: [Best: O(N lg N), Avg: O(N lg N), Worst:O(N^2)]
  *
  * # Recursive
  * # Divide and conquer algorithm
  * # Very efficient for large data sets
  *
  * 1. Pick a "pivot" element
  * 2. Partition array into 3 parts
  * 3. First - left, all elements in this part is less than "pivot"
  * 4. Second - the pivot itself and elements equals pivot
  * 5. Third - right all elements in this part is greater than or equal to the pivot
  * 6. Apply the algorithm to the all parts RECURSIVELY
  *
  * @see just for fun https://www.youtube.com/watch?v=3San3uKKHgg
  *
  **/
object QuickSort {


  /**
    * Left element "pivot"
    */
  def sort(arr: Array[Int]): Array[Int] =
    if (arr.length <= 1) arr
    else {
      val pivot = arr(arr.length / 2)
      val lessPivot = arr.filter(pivot>)
      val equalsPivot = arr.filter(pivot==)
      val largerPivot = arr.filter(pivot<)
      sort(lessPivot) ++ sort(equalsPivot) ++ sort(largerPivot)
    }

}
