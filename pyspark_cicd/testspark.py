import os
import sys
from operator import add

from pyspark import SparkContext

def do_word_counts(lines):

    counts = (lines.flatMap(lambda x: x.split())
                .map(lambda x: (x, 1))
                .reduceByKey(add)
             )
    results = {word: count for word, count in counts.collect()}
    return results


    """ count of words in an rdd of liness """

"""
    counts = text_file.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)

    results = {word: count for word, count in counts.collect()}

    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    return results
"""

if __name__ == "__main__":

    sc = SparkContext()
    print("first spark program")

#    text_file = sc.textFile("/home/lipu/Sample_Files/wordcount.txt")
    text_file = sc.textFile("D:\Sample files\wordcount.txt")
    print(do_word_counts(text_file))

