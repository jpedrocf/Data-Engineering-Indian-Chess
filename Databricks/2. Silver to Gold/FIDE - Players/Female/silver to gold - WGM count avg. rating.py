# Databricks notebook source
# MAGIC %md
# MAGIC - Dataframe creation of the table players_female_Base in the silver DB, using Spark

# COMMAND ----------

gm_avg_rating_df = spark.table('silver.players_female_base')

# COMMAND ----------

# MAGIC %md
# MAGIC - Filtering and counting active WGM players per country

# COMMAND ----------

from pyspark.sql import functions as F

# Filter out rows where the rating is 0 or null, the player is a WGM, and flag is not 'wi'
filtered_df = gm_avg_rating_df.filter(
    (gm_avg_rating_df.rating != 0) & 
    (gm_avg_rating_df.rating.isNotNull()) & 
    (gm_avg_rating_df.title == 'WGM') & 
    (gm_avg_rating_df.flag != 'wi')
)

# Group by country and calculate the average rating
average_rating_by_country = filtered_df.groupBy('country').agg(
    F.avg('rating').alias('average_rating'),
    F.count('*').alias('players')  # Add line_count column to count the number of lines per country
)

# Order by players count in descending order and round average_rating to 1 decimal place
average_rating_by_country = average_rating_by_country.orderBy(F.desc('players')).withColumn('average_rating', F.round('average_rating', 1))

# Display the result
display(average_rating_by_country)

# COMMAND ----------

average_rating_by_country.write.mode('overwrite').saveAsTable('gold.f_WGM_average_rating_by_country')
