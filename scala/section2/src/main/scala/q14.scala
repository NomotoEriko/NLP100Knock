import scala.io.StdIn

/**
  * Created by nomotoeriko on 2017/06/08.
  */
object q14 {
  def main(args: Array[String]): Unit = {
    var N = StdIn.readLine(">>>> N:").toInt
    val sentence = q10.load_sentence()
    if (N > sentence.length) N = sentence.length
    sentence.take(N).foreach(println)
  }
}
