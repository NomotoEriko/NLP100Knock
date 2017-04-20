/**
  * Created by nomotoeriko on 2017/04/20.
  */
object q09 {
  def main(args: Array[String]): Unit = {
    val str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    println(typoglycemia(str))
  }
  def typoglycemia(string: String): String = {
    def typo(word: String): String = word.replaceFirst("[^a-zA-Z]", "").length match {
      case 0 | 1 | 2 | 3 => word
      case _ => word.last match {
        case '.'|',' => (word.head.toString +: scala.util.Random.shuffle(word.tail.init.init.toList)
          ::: word.takeRight(2).toList).mkString("")
        case _ => (word.head.toString +: scala.util.Random.shuffle(word.tail.init.toList)
          :+ word.last.toString).mkString("")
      }
    }
    string.split(' ').map(word => typo(word)).mkString(" ")
  }
}
