file://<WORKSPACE>/train.scala
### java.lang.IndexOutOfBoundsException: -1

occurred in the presentation compiler.

presentation compiler configuration:


action parameters:
offset: 1016
uri: file://<WORKSPACE>/train.scala
text:
```scala
def youngest(df : Dataframe) : String {
    df.orderby("age").select("name").first().getString(0)
}

def youngest(df : Dataframe) : String {
    df.orderby("age").select("name").limit(10).collect().map(_.getString(0))
}

def getave(df : Dataframe) : Int {
    df.agg(avg("age")).getInt(0)
}


def moyRDD(rdd : RDD[Int]) : Double {
    val sum, count = rdd.map(value => (value, 1)).reduce((x, y) => (x._1 + y._1, x._2 + Y._2))
    sum / count
}


def filtreRDD(rdd : RDD[Int]) : RDD[Int] {
    rdd.filter(_ < 0)
}


given :class Student(name :String, birthday :Date, numberOfInternship: Int)
5) write a function that take an RDD[Student] and return the youngest student out of those who have the highest number of internship.


def young(rdd : RDD[Student]) : Student {
    val filt = rdd.orderby(numberOfInternship).select("name").limit(5).collect().map(getDouble(0))
    rdd.filter(_ != filt).orderby("age").first.getStudent(0)
}


def getYoungestTopInternStudent(rdd: RDD[Student]): Student = { 
    val max = rdd(@@)
}
```



#### Error stacktrace:

```
scala.collection.LinearSeqOps.apply(LinearSeq.scala:129)
	scala.collection.LinearSeqOps.apply$(LinearSeq.scala:128)
	scala.collection.immutable.List.apply(List.scala:79)
	dotty.tools.dotc.util.Signatures$.applyCallInfo(Signatures.scala:243)
	dotty.tools.dotc.util.Signatures$.computeSignatureHelp(Signatures.scala:101)
	dotty.tools.dotc.util.Signatures$.signatureHelp(Signatures.scala:88)
	dotty.tools.pc.SignatureHelpProvider$.signatureHelp(SignatureHelpProvider.scala:53)
	dotty.tools.pc.ScalaPresentationCompiler.signatureHelp$$anonfun$1(ScalaPresentationCompiler.scala:391)
```
#### Short summary: 

java.lang.IndexOutOfBoundsException: -1