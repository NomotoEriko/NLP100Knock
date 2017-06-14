/**
  * Created by nomotoeriko on 2017/04/24.
  */
import java.io.PrintWriter
object q36 {
  def main(args: Array[String]): Unit = {
    val word_counter = counter(q30.load_neko("../../data/neko.txt.mecab").reduce(_:::_))
    word_counter.toSeq.sortBy(-_._2).take(50).foreach(println)
    val file = new PrintWriter("all_word_counter.csv")
    word_counter.toSeq.foreach(s => file.write("%s, %d\n".format(s._1, s._2)))
    file.close()
  }

  def counter(sentence: List[Map[String, String]]): Map[String, Int] = {
    sentence.map(_("base")).groupBy(identity).mapValues(_.length)
  }
}
