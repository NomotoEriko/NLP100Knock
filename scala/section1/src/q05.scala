/**
  * Created by nomotoeriko on 2017/04/20.
  */
object q05 {
  def main(args: Array[String]): Unit = {
    val sentence = "I am an NLPer"
    make_ngram(2, sentence.split(' ').toList).foreach(x => print("(%s)".format(x.mkString(", "))))
    println()
    make_ngram(2, sentence.toList).foreach(x => print("(%s)".format(x.mkString(", "))))
  }
  def make_ngram(n: Int, seq: List[Any]): List[List[Any]]={
    var seqs = List.empty[List[Any]]
    for (i <- 0 until n) seqs  = seqs :+ seq.drop(i)
    var grams = List.empty[List[Any]]
    for (i <- seqs.last.indices) grams = grams :+ seqs.map(x => x(i))
    grams
  }
}
