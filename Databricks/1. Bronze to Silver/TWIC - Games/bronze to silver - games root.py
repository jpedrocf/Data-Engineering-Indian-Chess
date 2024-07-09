# Databricks notebook source
# MAGIC %md
# MAGIC # **Matches Table Root**

# COMMAND ----------

# MAGIC %md
# MAGIC - Dataframe creation of the table partidas_campeonato in the bronze DB, using Spark

# COMMAND ----------

games_df = spark.table('bronze.event_games')

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *
import datetime

# COMMAND ----------

# MAGIC %md
# MAGIC - Checking the schema for type adjustments

# COMMAND ----------

games_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC - Adjusting the types

# COMMAND ----------

schema = StructType([
    StructField("id", LongType(), False),
    StructField("event", StringType(), True),
    StructField("site", StringType(), True),
    StructField("date", DateType(), True),
    StructField("round", DoubleType(), True),
    StructField("white", StringType(),True),
    StructField("black", StringType(), True),
    StructField("result", StringType(), True),
    StructField("white_title", StringType(), True),
    StructField("black_title", StringType(), True),
    StructField("white_elo", LongType(), True),
    StructField("black_elo", LongType(), True),
    StructField("eco", StringType(), True),
    StructField("opening", StringType(), True),
    StructField("variation", StringType(), True),
    StructField("white_fide_id", IntegerType(), True),
    StructField("black_fide_id", IntegerType(), True),
    StructField("event_date", DateType(), True),
    StructField("moves", StringType(), True)
])

df_updated = spark.createDataFrame(games_df.rdd, schema)

df_updated.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC - Creating a new column of the result of the match, based on the result column and reordering the table

# COMMAND ----------

df_updated_with_new_col = df_updated.withColumn(
    "result_of_match",
    when(col("result") == "1/2-1/2", "Draw")
    .when(col("result") == "1-0", "White wins")
    .when(col("result") == "0-1", "Black wins")
    .otherwise("Unknown")
)

cols = df_updated_with_new_col.columns
new_cols_order = cols[:7] + ['result', 'result_of_match'] + cols[8:-1]
df_updated_with_new_col2 = df_updated_with_new_col.select(new_cols_order)

df_updated_with_new_col2.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC - Overwriting the table partidas_campeonato at the silver DB

# COMMAND ----------

df_updated_with_new_col2.write.mode('overwrite').saveAsTable('silver.event_games')
