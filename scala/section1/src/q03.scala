/**
  * Created by nomotoeriko on 2017/04/20.
  */
object q03 {
  def main(args: Array[String]): Unit = {
    val string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    val lens = (string split ' ').map(x => x.replaceFirst("[^a-zA-Z]+", "").length).toList
    println(lens)
  }
}
