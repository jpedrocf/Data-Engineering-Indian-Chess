# Databricks notebook source
# MAGIC %md
# MAGIC - Dataframe creation of the table players_male_Base in the silver DB, using Spark

# COMMAND ----------

avg_rating_df = spark.table('silver.players_male_base')

# COMMAND ----------

# MAGIC %md
# MAGIC - Filtering top 10 players per country, where flag is not inactive

# COMMAND ----------

from pyspark.sql import Window
from pyspark.sql import functions as F

# Filter out rows where the rating is 0 or null and the flag is not inactive
filtered_df = avg_rating_df.filter((avg_rating_df.rating != 0) & (avg_rating_df.rating.isNotNull()) & (avg_rating_df.flag.isNull()))

# Define a window specification to partition by country and order by rating descending
window_spec = Window.partitionBy('country').orderBy(F.desc('rating'))

# Add a row number within each partition
ranked_df = filtered_df.withColumn('rank', F.row_number().over(window_spec))

# Filter to keep only the top 10 players per country
top_10_df = ranked_df.filter(ranked_df.rank <= 10)

# Group by country and calculate the average rating of the top 10 players
average_rating_by_country = top_10_df.groupBy('country').agg(
    F.avg('rating').alias('average_rating')
)

# Order by average_rating in descending order and round to 1 decimal place
average_rating_by_country = average_rating_by_country.orderBy(F.desc('average_rating')).withColumn('average_rating', F.round('average_rating', 1))

# Display the result
display(average_rating_by_country)


# COMMAND ----------

average_rating_by_country.write.mode('overwrite').saveAsTable('gold.m_top10_average_rating_by_country')
