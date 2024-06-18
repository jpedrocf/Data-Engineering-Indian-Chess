# Databricks notebook source
# MAGIC %sql
# MAGIC select rating, flag, country
# MAGIC from silver.players
# MAGIC where rating > 2600 and flag is null

# COMMAND ----------

awesome_rated_players = spark.table('silver.players')

# COMMAND ----------

awesome_rated_players.printSchema()

# COMMAND ----------

from pyspark.sql import functions as F

# Filtra jogadores com rating maior que 2600
filtered_df_rating = awesome_rated_players.filter(awesome_rated_players.rating > 2600)

# Filtra a coluna 'flag' para remover registros com valor 'i'
filtered_df_rating2 = filtered_df_rating.filter(filtered_df_rating.flag.isNull())

# Agrupa por país e conta os jogadores
awesome_rated_players_by_country = filtered_df_rating2.groupBy('country').count()
awesome_rated_players_by_country2 = awesome_rated_players_by_country.withColumnRenamed("count", "player_count")

# Exibe o resultado
display(awesome_rated_players_by_country2)



# COMMAND ----------

awesome_rated_players_by_country2.write.mode('overwrite').saveAsTable('gold.2600_rated_players_per_country')
