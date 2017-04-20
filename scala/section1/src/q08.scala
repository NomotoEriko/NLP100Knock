/**
  * Created by nomotoeriko on 2017/04/20.
  */
object q08 {
  def main(args: Array[String]): Unit = {
    print(cipher("I am an NLPer"))
  }
  def cipher(str: String): String = {
    def cip(c: Char): Char = c.isLower match {
      case true => (219 - c).toChar
      case _ => c
    }
    str.map(x => cip(x))
  }
}
