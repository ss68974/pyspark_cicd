# Squash Test 1
import os
import sys
from operator import add

# Test change to trigger build in jenkins
# Squash Test 2
from pyspark import SparkContext, SparkConf

def do_word_counts(lines):
    """ count of words in an rdd of sushanta lines """

    counts = (lines.flatMap(lambda x: x.split())
        .map(lambda x: (x, 1))
        .reduceByKey(add)
        )

    results = {word: count for word, count in counts.collect()}
    return results


if __name__ == "__main__":

#    if len(sys.argv) != 2:
#        sys.exit("Usage: wordcount file}")

    sc = SparkContext(appName="PythonWordCount")
#    lines = sc.textFile(sys.argv[1], 1)
    lines = sc.textFile("D:\Sample Files\wordcount.txt", 1)

    print(do_word_counts(lines))
