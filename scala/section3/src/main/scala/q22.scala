/**
  * Created by nomotoeriko on 2017/06/09.
  */
object q22 {
  def main(args: Array[String]): Unit = {
    val text = q20.load_data()
    val pattern = ".*\\[\\[Category:(.+)\\]\\].*".r
    pattern.findAllMatchIn(text).map(_.group(1)).foreach(println)
  }
}
