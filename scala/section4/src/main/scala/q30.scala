/**
  * Created by nomotoeriko on 2017/04/23.
  */
object q30 {
  def main(args: Array[String]): Unit = {
    val neko = load_neko("../../data/neko.txt.mecab")
    println(neko.take(5))
  }

  def load_neko(path: String): List[List[Map[String, String]]] = {
    val neko = scala.io.Source.fromFile(path)
    val lines = neko.getLines()
    var sentence = List.empty[Map[String, String]]
    var mor_neko = List.empty[List[Map[String, String]]]
    for(l <- lines) l match {
      case "EOS" => if(sentence != Nil) {
        mor_neko = mor_neko :+ sentence
        sentence = List.empty[Map[String, String]]
      }
      case _ => sentence = sentence :+ get_morph(l)
    }
    neko.close()
    mor_neko
  }

  def get_morph(string: String): Map[String, String] = {
    val surface = string.split("\t")(0)
    val others = string.split("\t")(1).split(",")
    Map("surface" -> surface, "base" -> others(6), "pos" -> others(0), "pos1" -> others(1))
  }
}
