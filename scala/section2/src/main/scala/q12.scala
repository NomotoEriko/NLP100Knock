import java.io.File
import java.io.PrintWriter

import scala.io.Source

/**
  * Created by nomotoeriko on 2017/06/08.
  */
object q12 {
  def main(args: Array[String]): Unit = {
    val sentence = q10.load_sentence()
    val col1 = new PrintWriter(new File("col1.txt"))
    val col2 = new PrintWriter(new File("col2.txt"))

    sentence.foreach(x => col1.write(x.split("\t").head+"\n"))
    sentence.foreach(x => col2.write(x.split("\t").tail.head+"\n"))
    col1.close()
    col2.close()
  }
}
