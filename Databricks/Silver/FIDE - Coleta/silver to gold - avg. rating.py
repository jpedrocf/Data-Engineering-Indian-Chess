# Databricks notebook source
# MAGIC %sql
# MAGIC select *
# MAGIC from silver.players

# COMMAND ----------

avg_rating_df = spark.table('silver.players')

# COMMAND ----------

avg_rating_df.printSchema()

# COMMAND ----------

from pyspark.sql import functions as F

# Filter out rows where the rating is 0 or null
filtered_df = avg_rating_df.filter((avg_rating_df.rating != 0) & (avg_rating_df.rating.isNotNull()))

# Group by country and calculate the average rating
average_rating_by_country = filtered_df.groupBy('country').agg(
    F.avg('rating').alias('average_rating'),
    F.count('*').alias('line_count')  # Add line_count column to count the number of lines per country
)

# Order by average_rating in descending order and round to 1 decimal place
average_rating_by_country = average_rating_by_country.orderBy(F.desc('average_rating')).withColumn('average_rating', F.round('average_rating', 1))

# Display the result
display(average_rating_by_country)

# COMMAND ----------

average_rating_by_country.write.mode('append').saveAsTable('gold.average_rating_by_country')
