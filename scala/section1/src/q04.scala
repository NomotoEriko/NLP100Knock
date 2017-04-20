/**
  * Created by nomotoeriko on 2017/04/20.
  */
object q04 {
  def main(args: Array[String]): Unit = {
    val string = "Hi He Lied Because Boron Could Not Oxidize Fluorine." +
      " New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    var m = Map.empty[Int, String]
    for (i <- string.split(' ').indices) i match {
      case 1|5|6|7|8|9|15|16|19 => m += (i -> string.split(' ')(i).take(1))
      case _ => m += (i -> string.split(' ')(i).take(2))
    }
    print_map(m)
  }
  def print_map(m: Map[Int, String]): Unit ={
    for (i <- m.keys.toList.sorted) println("%2d: %s".format(i, m(i)))
  }
}
