import scala.io.Source
import vegas._

/**
  * Created by nomotoeriko on 2017/06/13.
  */
object q37 {
  def main(args: Array[String]): Unit = {
    val m = load_word_frequency().toSeq.sortBy(-_._2).take(10)
//    m.foreach(println)
    val plot = Vegas("top 10 word frepuency").withData(
      m.map(x => Map("word" -> x._1, "flequency" -> x._2))
    ).encodeX("word", Nom).encodeY("flequency", Quant).mark(Bar)
    plot.show
  }

  def load_word_frequency(csv_path: String = "all_word_counter.csv"): Map[String,Int] = {
    var m = Map.empty[String, Int]
    for (line <- Source.fromFile(csv_path).getLines()) {
      val p = line.split(", ")
      if (p.length == 2) m = m + (p.apply(0) -> p.apply(1).toInt)
    }
    m
  }
}
