# Databricks notebook source
## CÓDIGO PARA CONTAGEM DE GM'S ATIVOS E INATIVOS POR PAÍS

# COMMAND ----------

players_df = spark.table('silver.players')

# COMMAND ----------

display(players_df)

# COMMAND ----------

from pyspark.sql.functions import count, when, col

filteredgm_df = players_df.filter((players_df.title == 'GM') | (players_df.title == 'WGM'))
count_by_country = filteredgm_df.groupBy('country').agg(
    count(when(col('flag').isNull(), True)).alias('Actives'),
    count(when(col('flag').isNotNull(), True)).alias('Inactives')
).orderBy(col('Actives').desc())

display(count_by_country)

# COMMAND ----------

count_by_country.printSchema()

# COMMAND ----------

count_by_country.write.mode('append').saveAsTable('gold.gms_by_country')
