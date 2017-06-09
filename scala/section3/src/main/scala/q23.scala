/**
  * Created by nomotoeriko on 2017/06/09.
  */
object q23 {
  def main(args: Array[String]): Unit = {
    val text = q20.load_data()
    val pattern = "(={2,})([^=\n]+)(={2,})".r
    pattern.findAllMatchIn(text).map(x => (x.group(2), x.group(1).length-1)).foreach(println)
  }
}
