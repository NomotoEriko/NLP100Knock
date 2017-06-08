/**
  * Created by nomotoeriko on 2017/06/08.
  */
object q19 {
  def main(args: Array[String]): Unit = {
    val data = q10.load_sentence()
    data.groupBy(_.split("\t").head).toSeq.map(_._2).sortBy(_.length).reverse.reduce(_:::_).foreach(println)
  }
}
