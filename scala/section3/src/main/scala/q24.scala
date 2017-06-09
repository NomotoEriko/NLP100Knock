/**
  * Created by nomotoeriko on 2017/06/09.
  */
object q24 {
  def main(args: Array[String]): Unit = {
    val text = q20.load_data()
    val pattern = "(ファイル|File|file):([^|]+)\\|".r
    pattern.findAllMatchIn(text).map(_.group(2)).foreach(println)
  }
}
