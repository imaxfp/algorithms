package other.fcombinators

import org.scalatest.FunSuite


/**
  * Created by maxim on 3/19/17.
  */
class FunctionalCombinatorsImplicit$Test extends FunSuite {

  test("Implicit conversion") {
    //Before giving up, though, compiler searches for an implicit conversion from Double to Int
    //The compiler then inserts a call to doubleToInt automatically. Behind the scenes, the code becomes: val i: Int = doubleToInt(3.5)
    //idea to have something that causes a loss in precision happen invisibly. So this is not really a conversion we recommend.
    import FunctionalCombinatorsImplicit.doubleToInt
    val toInt: Int = 3.5
    import FunctionalCombinatorsImplicit.intToString
    val toStr: String = 11
  }

  test ("Implicit rich wrappers pattern") {
    import FunctionalCombinatorsImplicit.ArrowAssoc2
    //Use of implicit conversions is to simulate adding new syntax. Recall that you can make a Map using syntax like this:
    //In other languages might feel the need to develop an external DSL.
    Map(1 -> "one", 2 -> "two")
    Map(1 ---> "one", 2 ---> "two")
  }


  test ("Implicit parameters") {
    import FunctionalCombinatorsImplicit._

  }

}
