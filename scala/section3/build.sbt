name := "section3"

version := "1.0"

scalaVersion := "2.10.4"

scalacOptions ++= Seq("-Xlint", "-deprecation", "-unchecked")

incOptions := incOptions.value.withNameHashing(true)

libraryDependencies ++= Seq(
  "org.json4s" %% "json4s-native" % "3.2.8",
  "org.scalatest" %% "scalatest" % "2.1.3" % "test"
)