/**
  * Created by nomotoeriko on 2017/04/24.
  */
object q34 {

  def main(args: Array[String]): Unit = {
    val neko = q30.load_neko("../../data/neko.txt.mecab")
    val result = noun_no_noun(neko)
    result.foreach(println)
  }

  def noun_no_noun(neko: List[List[Map[String, String]]]): Set[String] = {
    neko.map(sentence => get_noun_no_noun(sentence)).reduce(_|_)
  }

  def get_noun_no_noun(sentence: List[Map[String, String]]): Set[String] = {
    val idx = (0 until sentence.length-2).toList.filter(i => sentence(i)("pos")=="名詞")
      .filter(i => sentence(i+1)("surface")=="の")
      .filter(i => sentence(i+2)("pos")=="名詞")
    idx.map(i => sentence(i)("surface")+sentence(i+1)("surface")+sentence(i+2)("surface")).toSet
  }
}
