import os
import sys

from pyspark import SparkContext, SparkConf

sc = SparkContext()

print('First Spark Program')

text_file = sc.textFile("D:\Sample files\\wordcount.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
for x in counts.collect():
    print(x)


