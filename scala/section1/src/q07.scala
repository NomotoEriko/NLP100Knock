/**
  * Created by nomotoeriko on 2017/04/20.
  */
object q07 {
  def main(args: Array[String]): Unit = {
    println(temprate(12, "気温", 22.4))
  }
  def temprate(x: Any, y: Any, z:Any): String = {
    "%s時の%sは%s".format(x, y, z)
  }
}
