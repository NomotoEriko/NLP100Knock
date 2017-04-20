/**
  * Created by nomotoeriko on 2017/04/20.
  */
object q02 {
  def main(args: Array[String]): Unit = {
    val s1 = "パトカー"
    val s2 = "タクシー"
    var string = ""
    for (i <- 0 until List(s1.length, s2.length).min) string = string :+ s1(i) :+ s2(i)
    println(string)
  }
}
