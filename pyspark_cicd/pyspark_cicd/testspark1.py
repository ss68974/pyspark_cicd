from operator import add
# Test Commit 3

from pyspark import SparkContext

def do_word_counts(lines):
    """ count of words in an rdd of sushanta linesss """

    counts = (lines.flatMap(lambda x: x.split())
        .map(lambda x: (x, 1))
        .reduceByKey(add)
        )

    results = {word: count for word, count in counts.collect()}
    return results


if __name__ == "__main__":

    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile("D:\Sample Files\wordcount.txt", 1)

    print(do_word_counts(lines))
