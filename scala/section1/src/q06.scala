/**
  * Created by nomotoeriko on 2017/04/20.
  */
object q06 {
  def main(args: Array[String]): Unit = {
    val sentence1 = "paraparaparadise"
    val sentence2 = "paragraph"
    val X = q05.make_ngram(2, sentence1.toList).toSet
    val Y = q05.make_ngram(2, sentence2.toList).toSet
    println("X ∪ Y: %s".format(X|Y))
    println("X ∩ Y: %s".format(X&Y))
    println("X - Y: %s".format(X.diff(Y)))
    println("X contains se: %s".format(X("se".toList)))
    println("Y contains se: %s".format(Y("se".toList)))
  }
}
