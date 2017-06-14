import vegas._
import scala.math._
/**
  * Created by nomotoeriko on 2017/06/14.
  */
object q39 {
  def main(args: Array[String]): Unit = {
    val frequency = q37.load_word_frequency().toSeq.sortBy(-_._2).map(_._2)
    val data = (1 until frequency.length).map(i => Map("val" -> log(frequency.apply(i-1)), "order" -> log(i)))
    Vegas("Zipf").
      withData(data).
      mark(Line).
      encodeX("order", Quant).
      encodeY("val", Quant).show
  }
}
