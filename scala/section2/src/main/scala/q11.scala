//import q10.load_sentence
/**
  * Created by nomotoeriko on 2017/06/08.
  */
object q11 {
  def main(args: Array[String]): Unit = {
    val sentence = q10.load_sentence()
    var new_sentence = List.empty[String]
    for (line <- sentence) new_sentence = new_sentence :+ line.replace("\t", " ")
    new_sentence.foreach(println)
  }
}
