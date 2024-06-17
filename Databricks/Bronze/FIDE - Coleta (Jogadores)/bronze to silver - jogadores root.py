# Databricks notebook source
players_df = spark.table('bronze.players_complete')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM bronze.players_complete

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *
import datetime

# COMMAND ----------

player_com_date = players_df.withColumn('version_date', lit('2024-06-06'))

# COMMAND ----------

from pyspark.sql.functions import to_date

player_com_date = player_com_date.withColumn('version_date', to_date('version_date'))

# COMMAND ----------

display(player_com_date)

# COMMAND ----------

player_com_date.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col

players_transform_type = player_com_date.filter(col('fideid').isNotNull()).withColumn('fideid', col('fideid').cast('integer'))

# COMMAND ----------

# MAGIC %md
# MAGIC CHECKING IF WHEN SEX = F THAT IS A MALE TITLE WHILE COUNTING AND REPLACING THE ERRORS

# COMMAND ----------

# DBTITLE 1,CORRECTING TITLES - FEMALE
from pyspark.sql.functions import col, when, udf
from pyspark.sql.types import IntegerType

# Inicializar um contador
substitution_counter = spark.sparkContext.accumulator(0)

# Definir uma UDF para contar as substituições
def count_substitution(title, sex):
    global substitution_counter
    if sex == 'F' and title in ['GM', 'IM', 'FM', 'CM']:
        substitution_counter.add(1)
    return title

count_substitution_udf = udf(count_substitution, StringType())

# Aplicar as substituições e contar
players_transform_type = player_com_date.withColumn(
    'title',
    when((col('sex') == 'F') & (col('title') == 'GM'), 'WGM')
    .when((col('sex') == 'F') & (col('title') == 'IM'), 'WIM')
    .when((col('sex') == 'F') & (col('title') == 'FM'), 'WFM')
    .when((col('sex') == 'F') & (col('title') == 'CM'), 'WCM')
    .otherwise(col('title'))
)

# Aplicar a UDF para contar as substituições
players_transform_type = players_transform_type.withColumn(
    'title', count_substitution_udf(col('title'), col('sex'))
)

# Mostrar o contador de substituições
print(f"Total de substituições: {substitution_counter.value}")

# COMMAND ----------

display(players_transform_type)

# COMMAND ----------

# MAGIC %md
# MAGIC CHECKING IF WHEN SEX = M THAT IS A FEMALE TITLE WHILE COUNTING AND REPLACING THE ERRORS

# COMMAND ----------

# DBTITLE 1,CORRECTING TITLES - MALE
from pyspark.sql.functions import col, when, udf
from pyspark.sql.types import IntegerType

# Inicializar um contador
substitution_counter2 = spark.sparkContext.accumulator(0)

# Definir uma UDF para contar as substituições
def count_substitution(title, sex):
    global substitution_counter2
    if sex == 'M' and title in ['WGM', 'WIM', 'WFM', 'WCM']:
        substitution_counter2.add(1)
    return title

count_substitution_udf2 = udf(count_substitution, StringType())

# Aplicar as substituições e contar
players_transform_type = players_transform_type.withColumn(
    'title',
    when((col('sex') == 'M') & (col('title') == 'WGM'), 'GM')
    .when((col('sex') == 'M') & (col('title') == 'WIM'), 'IM')
    .when((col('sex') == 'M') & (col('title') == 'WFM'), 'FM')
    .when((col('sex') == 'M') & (col('title') == 'WCM'), 'CM')
    .otherwise(col('title'))
)

# Aplicar a UDF para contar as substituições
players_transform_type = players_transform_type.withColumn(
    'title', count_substitution_udf2(col('title'), col('sex'))
)

# Mostrar o DataFrame resultante
players_transform_type.show()

# Mostrar o contador de substituições
print(f"Total de substituições: {substitution_counter2.value}")

# COMMAND ----------

# DBTITLE 1,CORRECTING FLAGS - FEMALE
from pyspark.sql.functions import col, when, udf
from pyspark.sql.types import StringType

substitution_counter_flag = spark.sparkContext.accumulator(0)

def count_flag_substitution(flag, sex):
    global substitution_counter_flag
    if sex == 'F' and flag == 'I':
        substitution_counter_flag.add(1)
        return 'WI'
    return flag

count_flag_substitution_udf = udf(count_flag_substitution, StringType())


players_transform_flag = players_transform_type.withColumn(
    'flag', count_flag_substitution_udf(col('flag'), col('sex'))
)


players_transform_flag.show()


print(f"Total de substituições: {substitution_counter_flag.value}")

# COMMAND ----------

# DBTITLE 1,CORRECTING FLAGS - MALE
from pyspark.sql.functions import col, when, udf
from pyspark.sql.types import StringType

substitution_counter_flag = spark.sparkContext.accumulator(0)

def count_flag_substitution(flag, sex):
    global substitution_counter_flag
    if sex == 'M' and flag == 'WI':
        substitution_counter_flag.add(1)
        return 'I'
    return flag

count_flag_substitution_udf = udf(count_flag_substitution, StringType())


players_transform_flag = players_transform_type.withColumn(
    'flag', count_flag_substitution_udf(col('flag'), col('sex'))
)


players_transform_flag.show()


print(f"Total de substituições: {substitution_counter_flag.value}")

# COMMAND ----------

players_transform_flag.printSchema()

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.types import LongType

spark = SparkSession.builder.appName("NonNullableTransformation").getOrCreate()

players_df_final = players_transform_flag.fillna({"fideid": 0})

players_df_final = players_df_final.withColumn("fideid", players_df_final["fideid"].cast(LongType()))

players_df_final.printSchema()



# COMMAND ----------

display(players_df_final)

# COMMAND ----------

players_df_final.write.mode('overwrite').saveAsTable('silver.players_colunas')
