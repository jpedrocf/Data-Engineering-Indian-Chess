# Databricks notebook source
df = spark.table('complete_list_players')

# COMMAND ----------

display(df)

# COMMAND ----------

display(df.groupBy('file_name').count())

# COMMAND ----------



# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

df2 = df.withColumn('date_of_rating', regexp_replace("file_name", r"\.xml$", "")).withColumn('date_of_rating',to_date(col("date_of_rating"), "yyyyMM"))

# COMMAND ----------

display(df2)

# COMMAND ----------

df3 = df2.withColumn('month_name', date_format('date_of_rating', 'MMM/yyyy'))
display(df3.groupBy('month_name').count())
