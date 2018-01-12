from setuptools import setup

setup(
    name='pyspark_cicd',
    version='1.0.0',
    packages=['py4j', 'py4j.tests', 'pyspark', 'pyspark.ml', 'pyspark.ml.param', 'pyspark.ml.linalg', 'pyspark.sql',
              'pyspark.mllib', 'pyspark.mllib.stat', 'pyspark.mllib.linalg', 'pyspark.streaming'],
    url='',
    license='',
    author='susha',
    author_email='sushanta.samantaray@gmail.com',
    description='Pyspark ci cd testing automation', install_requires=['pytest']
)
