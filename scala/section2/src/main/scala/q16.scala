import scala.io.StdIn

/**
  * Created by nomotoeriko on 2017/06/08.
  */
object q16 {
  def main(args: Array[String]): Unit = {
    var N = StdIn.readLine(">>>> N: ").toInt
    val sentence = q10.load_sentence()
    if (N > sentence.length) N = sentence.length

    val d_num = sentence.length / N
    val border = sentence.length % N
    var result = List.empty[List[String]]
    var c = 0
    for (i <- 0.until(N)){
      val data = if(i < border)d_num+1 else d_num
      result = result :+ sentence.slice(c, c+data)
      c = c + data
    }
    result.foreach(x => (("-"*40)+:x).foreach(println))
  }
}
