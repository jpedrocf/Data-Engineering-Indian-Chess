# Databricks notebook source
# MAGIC %md
# MAGIC - Dataframe creation of the table players_male_Base in the silver DB, using Spark

# COMMAND ----------

gm_avg_rating_df = spark.table('silver.players_male_base')

# COMMAND ----------

# MAGIC %md
# MAGIC - Filtering and counting active GM players per country

# COMMAND ----------

from pyspark.sql import functions as F

# Filter out rows where the rating is 0 or null, the player is not a GM, or the flag is null
filtered_df = gm_avg_rating_df.filter(
    (gm_avg_rating_df.rating != 0) & 
    (gm_avg_rating_df.rating.isNotNull()) & 
    (gm_avg_rating_df.title == 'GM') & 
    (gm_avg_rating_df.flag.isNull())
)

# Group by country and calculate the average rating
average_rating_by_country = filtered_df.groupBy('country').agg(
    F.avg('rating').alias('average_rating'),
    F.count('*').alias('players')  # Add line_count column to count the number of lines per country
)

# Order by players count in descending order and average_rating in descending order
average_rating_by_country = average_rating_by_country.orderBy(F.desc('players'), F.desc('average_rating')).withColumn('average_rating', F.round('average_rating', 1))

# Display the result
display(average_rating_by_country)

# COMMAND ----------

average_rating_by_country.write.mode('overwrite').saveAsTable('gold.M_GM_average_rating_by_country')
