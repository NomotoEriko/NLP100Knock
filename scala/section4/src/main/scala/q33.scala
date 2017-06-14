/**
  * Created by nomotoeriko on 2017/04/24.
  */
object q33 {
  def main(args: Array[String]): Unit = {
    val neko = q30.load_neko("../../data/neko.txt.mecab")
    val nouns = get_noun(neko)
    nouns.foreach(println)
  }

  def get_noun(neko: List[List[Map[String, String]]]): Set[String] = {
    neko.map(sentence => sentence.filter(_("pos")=="名詞").filter(_("pos1") == "サ変接続")
      .map(_("base"))).reduce(_:::_).toSet
  }
}
