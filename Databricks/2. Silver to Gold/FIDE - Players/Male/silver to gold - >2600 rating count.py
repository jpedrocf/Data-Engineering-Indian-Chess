# Databricks notebook source
# MAGIC %md
# MAGIC - Dataframe creation of the table players_male_Base in the silver DB, using Spark

# COMMAND ----------

awesome_rated_players = spark.table('silver.players_male_base')

# COMMAND ----------

# MAGIC %md
# MAGIC - Filtering active male players with more than 2600 of rating and counting them in descending order per country

# COMMAND ----------

from pyspark.sql import functions as F

#Filter out rows where the rating is under 2600 and the flag is not null (inactive players)
filtered_df_rating = awesome_rated_players.filter((awesome_rated_players.rating > 2600) & (awesome_rated_players.flag.isNull()))

#Grouping them by country and counting in descending order
awesome_rated_players_by_country = filtered_df_rating.groupBy('country').count()
awesome_rated_players_by_country2 = awesome_rated_players_by_country.withColumnRenamed("count", "player_count")

awesome_rated_players_by_country2 = awesome_rated_players_by_country2.orderBy(F.desc("player_count"))

display(awesome_rated_players_by_country2)

# COMMAND ----------

awesome_rated_players_by_country2.write.mode('overwrite').saveAsTable('gold.m_2600_rated_players_per_country')
