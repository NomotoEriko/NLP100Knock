import java.io.{File, PrintWriter}

/**
  * Created by nomotoeriko on 2017/06/08.
  */
object q13 {
  def main(args: Array[String]): Unit = {
    val col1 = q10.load_sentence("col1.txt")
    val col2 = q10.load_sentence("col2.txt")
    val col12 = new PrintWriter(new File("col12.txt"))

    for (i <- col1.indices) col12.write(col1.apply(i)+"\t"+col2.apply(i)+"\n")
    col12.close()
  }
}
