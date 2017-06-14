/**
  * Created by nomotoeriko on 2017/04/24.
  */
object q32 {
  def main(args: Array[String]): Unit = {
    val neko = q30.load_neko("../../data/neko.txt.mecab")
    val varbs = get_varb(neko)
    varbs.foreach(println)
  }

  def get_varb(neko: List[List[Map[String, String]]]): Set[String] = {
    neko.map(sentence => sentence.filter(morph => morph("pos")=="動詞").map(_("base"))).reduce(_:::_).toSet
  }
}
