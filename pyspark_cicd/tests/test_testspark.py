import pytest
from pyspark_cicd.pyspark_cicd import testspark

#print('11111')

# this allows using the fixture in all tests in this module
#pytestmark = pytest.mark.usefixtures("spark_context")


# Can also use a decorator such as this to use specific fixtures in specific functions
@pytest.mark.usefixtures("spark_context")


def test_do_word_counts(spark_context):
    """ test that a single event is parsed correctly
    Args:
        spark_context: test fixture SparkContext
        hive_context: test fixture HiveContext
    """

    test_input = [
        ' hello spark ',
        ' hello again spark spark'
    ]

    input_rdd = spark_context.parallelize(test_input, 1)
    results = testspark.do_word_counts(input_rdd)

    expected_results = {'hello': 2, 'spark': 3, 'again': 1}
    assert results == expected_results
