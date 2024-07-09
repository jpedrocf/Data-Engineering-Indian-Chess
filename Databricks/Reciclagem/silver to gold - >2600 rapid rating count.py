# Databricks notebook source
# MAGIC %sql
# MAGIC select rapid_rating, flag, country
# MAGIC from silver.players_jun24
# MAGIC where rapid_rating > 2700 and flag is null

# COMMAND ----------

awesome_rated_players = spark.table('silver.players')

# COMMAND ----------

awesome_rated_players.printSchema()

# COMMAND ----------

from pyspark.sql import functions as F

filtered_df_rating = awesome_rated_players.filter(awesome_rated_players.rapid_rating > 2600)

filtered_df_rating2 = filtered_df_rating.filter(filtered_df_rating.flag.isNull())

awesome_rated_players_by_country = filtered_df_rating2.groupBy('country').count()
awesome_rated_players_by_country2 = awesome_rated_players_by_country.withColumnRenamed("count", "player_count")


display(awesome_rated_players_by_country2)



# COMMAND ----------

awesome_rated_players_by_country2.write.mode('overwrite').saveAsTable('gold.2600_rapid_rated_players_per_country')
