# Databricks notebook source
from databricks.connect import DatabricksSession

import {{cookiecutter.package_name}}

{{cookiecutter.package_name}}.main()

spark = DatabricksSession.builder.getOrCreate()
df = spark.range(10)
display(df)