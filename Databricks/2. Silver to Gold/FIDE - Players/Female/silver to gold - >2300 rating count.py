# Databricks notebook source
# MAGIC %md
# MAGIC - Dataframe creation of the table players_female_Base in the silver DB, using Spark

# COMMAND ----------

awesome_rated_players = spark.table('silver.players_female_base')

# COMMAND ----------

# MAGIC %md
# MAGIC - Filtering active female players with more than 2300 of rating and counting them in descending order per country

# COMMAND ----------

from pyspark.sql import functions as F

filtered_df_rating = awesome_rated_players.filter(awesome_rated_players.rating > 2300)

filtered_df_rating2 = filtered_df_rating.filter(filtered_df_rating.flag != 'wi')

awesome_rated_players_by_country = filtered_df_rating2.groupBy('country').count()
awesome_rated_players_by_country2 = awesome_rated_players_by_country.withColumnRenamed("count", "player_count")

awesome_rated_players_by_country2 = awesome_rated_players_by_country2.orderBy(F.desc("player_count"))

display(awesome_rated_players_by_country2)

# COMMAND ----------

awesome_rated_players_by_country2.write.mode('overwrite').saveAsTable('gold.F_2300_rated_players_per_country')
