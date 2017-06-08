/**
  * Created by nomotoeriko on 2017/06/08.
  */
object q18 {
  def main(args: Array[String]): Unit = {
    val data = q10.load_sentence()
    data.sortBy(_.split("\t").apply(2).toDouble).reverse.foreach(println)
  }
}
