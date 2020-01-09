from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg, sum, min, max

spark = SparkSession\
        .builder\
        .master("local")\
        .appName("SparkBatchProcessing")\
        .getOrCreate()

csvFile = spark.read.format("csv").option("header","false").option("inferSchema","true").load("Data.csv")  #load the csv file

csvFile.show() #print the matrix of the Data.csv

csvFile.select(sum("_c1").alias("Sum_c1"),avg("_c1").alias("Avg_c1"),min("_c1").alias("Min_c1"),max("_c1").alias("Max_c1")).show()  #print these statistics of second column: summary, average, minimun element, maximun element
