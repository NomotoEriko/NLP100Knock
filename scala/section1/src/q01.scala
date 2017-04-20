/**
  * Created by nomotoeriko on 2017/04/20.
  */
object q01 {
  def main(args: Array[String]): Unit = {
    val string = "パタトクカシーー"
    var s = ""
    for (i <- 0 until string.length by 2) s = s :+ string(i)
    println(s)
  }
}
