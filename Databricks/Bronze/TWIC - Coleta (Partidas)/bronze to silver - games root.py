# Databricks notebook source
# MAGIC %sql
# MAGIC select *
# MAGIC from bronze.partidas_campeonato

# COMMAND ----------

games_df = spark.table('bronze.partidas_campeonato')

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *
import datetime

# COMMAND ----------

games_df.printSchema()

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
    StructField("white_fide_id", StringType(), True),
    StructField("black_fide_id", StringType(), True),
    StructField("event_date", DateType(), True),
    StructField("moves", StringType(), True)
])

df_updated = spark.createDataFrame(games_df.rdd, schema)

df_updated.printSchema()

# COMMAND ----------

df_updated_with_new_col = df_updated.withColumn(
    "result_of_match",
    when(col("result") == "1/2-1/2", "Draw")
    .when(col("result") == "1-0", "White wins")
    .when(col("result") == "0-1", "Black wins")
    .otherwise("Unknown")
)

cols = df_updated_with_new_col.columns
new_cols_order = cols[:7] + ['result', 'result_of_match'] + cols[8:]
df_updated_with_new_col2 = df_updated_with_new_col.select(new_cols_order)

df_updated_with_new_col2.printSchema()

# COMMAND ----------

all_columns = df_updated_with_new_col2.columns

columns_to_keep = all_columns[:-1]

df_updated_with_new_col2 = df_updated_with_new_col2.select(*columns_to_keep)

df_updated_with_new_col2.printSchema()

# COMMAND ----------

df_updated_with_new_col2.write.mode('overwrite').saveAsTable('silver.partidas_campeonato')
