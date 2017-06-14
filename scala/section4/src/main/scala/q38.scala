import vegas._
//import vegas.render.WindowRenderer._
/**
  * Created by nomotoeriko on 2017/06/14.
  */
object q38 {
  def main(args: Array[String]): Unit = {
    val m = q37.load_word_frequency().toSeq.map(_._2).groupBy(n => n).
      toSeq.map(n => (n._1, n._2.length)).filter(n => n._2 < 100).filter(n => n._1 > 10).filter(n => n._1 < 100).
      map(x => Map("frequency" -> x._1, "kinds of word" -> x._2))
    Vegas("histogram").
      withData(m).
      mark(Bar).
      encodeX("frequency", Quant).
      encodeY("kinds of word",  Quant).show
  }
}
