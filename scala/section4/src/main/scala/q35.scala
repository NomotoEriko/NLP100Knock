import scala.collection.JavaConverters._

/**
  * Created by nomotoeriko on 2017/04/24.
  */
object q35 {
  def main(args: Array[String]): Unit = {
    val neko = q30.load_neko("../../data/neko.txt.mecab")
    longer_noun(neko).foreach(println)
  }

  def longer_noun(neko: List[List[Map[String, String]]]): Set[String] = {
    neko.map(sentence => continuity_noun(sentence)).reduce(_|_)
  }

  def continuity_noun(sentence: List[Map[String, String]]): Set[String] = {
    val noun_idx = sentence.indices.filter(i => sentence(i)("pos") == "名詞").toList
    val continuity_noun_idx = get_continuity(noun_idx)
    continuity_noun_idx.map(ints => ints.map(i => sentence(i)("surface")).mkString("")).toSet
  }

  def get_continuity(ints: List[Int]): List[List[Int]] = {
    var list_ints = List.empty[List[Int]]
    var block = List.empty[Int]
    for(i <- ints){
      block = block :+ i
      if(!ints.contains(i+1)){
        list_ints = list_ints :+ block
        block = List.empty[Int]
      }
    }
    list_ints
  }
}
