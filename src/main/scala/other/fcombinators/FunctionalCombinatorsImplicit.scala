package other.fcombinators

/**
  * Created by Maxim.
  *
  * Own implementation of the functional combinators like map, filter, fold, e.t.c.
  *
  * @see Implicit Design Pattern
  * http://www.lihaoyi.com/post/ImplicitDesignPatternsinScala.html
  */
object FunctionalCombinatorsImplicit {

  implicit def doubleToInt(x: Double): Int = x.toInt
  implicit def intToString(x: Int): String = x.toString
  implicit def int2double(x: Int): Double = x.toDouble

  implicit final class ArrowAssoc2[A](private val self: A) extends AnyVal {
    @inline def ---> [B](y: B): Tuple2[A, B] = Tuple2(self, y)
    def →[B](y: B): Tuple2[A, B] = --->(y)
  }

  /**
    * merge list algorithm.
    * Each of the lists sorted from min to max
    *
    */

  def map[A](a: List[A], f: A => A): List[A] = {
    a.map(e => f(e))
    var res = a


    res
  }

}
