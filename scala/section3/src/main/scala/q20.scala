import org.json4s.JsonAST.{JField, JObject, JString}
import org.json4s.native.JsonMethods

import scala.io.Source

/**
  * Created by nomotoeriko on 2017/06/08.
  */
object q20 {
  def main(args: Array[String]): Unit = {
    val data = load_data()
    print(data)
  }

  def load_data(path: String = "../../data/jawiki-country.json"): String = {
    val json = Source.fromFile(path).getLines().mkString.replace("\\n", "\n")
    val json_value = JsonMethods.parse("["+json+"]")
    val uk = for {
      JObject(child) <- json_value
      JField("title", JString(title)) <- child
      JField("text", JString(text)) <- child
      if title == "イギリス"
    } yield text
    uk.reduce(_+_)
  }
}
