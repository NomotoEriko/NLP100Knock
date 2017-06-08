import scala.io.Source

/**
  * Created by nomotoeriko on 2017/06/08.
  */
object q10 {
  def main(args: Array[String]): Unit = {
    val sentence = load_sentence()
    println(sentence.length)
  }

  def load_sentence(path: String = "http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt"): List[String] = {
    var sentence = List.empty[String]
    if ("http" == path.take(4)){
      for (line <- Source.fromURL(path).getLines()) sentence = sentence :+ line
    }else{
      for (line <- Source.fromFile(path).getLines()) sentence = sentence :+ line
    }
    sentence
  }
}
