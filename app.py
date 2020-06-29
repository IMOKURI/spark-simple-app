import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Version app").setMaster("yarn")
sc = SparkContext(conf=conf)

if sys.version_info[0] == 3:
    print("Python 3")
elif sys.version_info[0] == 2:
    print("Python 2")
