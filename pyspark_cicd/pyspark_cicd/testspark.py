import os
import sys

from pyspark import SparkContext, SparkConf

def do_word_counts():
    """ count of words in an rdd of sushanta lines """

    sc = SparkContext()

    print("first spark program")

    text_file = sc.textFile("D:\Sample files\\wordcount.txt")

    counts = text_file.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)

    results = {word: count for word, count in counts.collect()}

    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    return results

if __name__ == "__main__":

    do_word_counts()
