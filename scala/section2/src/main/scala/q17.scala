/**
  * Created by nomotoeriko on 2017/06/08.
  */
object q17 {
  def main(args: Array[String]): Unit = {
    val col1 = q10.load_sentence("col1.txt").toSet
    col1.foreach(println)
    println("種類数: %d".format(col1.size))
  }
}
