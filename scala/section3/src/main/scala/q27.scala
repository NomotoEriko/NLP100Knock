/**
  * Created by nomotoeriko on 2017/06/09.
  */
object q27 {
  def main(args: Array[String]): Unit = {
    val text = q20.load_data().split("\n")
    val pattern1 = "'{2,}"
    val pattern2 = "\\[\\[([^\\]]*)\\|"
    val infomation = text.slice(text.indexWhere(_.take(6) == "{{基礎情報")+1, text.indexWhere(_.take(2) == "}}")).
      reduce(_+"\n"+_).replaceAll(pattern1, "").replaceAll(pattern2, "").
      replaceAll("\\[\\[", "").replaceAll("\\]\\]", "").tail.split("\n\\|").toList.map(_.split(" = ").toList)
    infomation.foreach(println)
  }
}
