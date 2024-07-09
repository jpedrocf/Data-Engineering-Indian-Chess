# Databricks notebook source
# MAGIC %md
# MAGIC # **Current Month Players Table**
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC - Dataframe creation of the table players in the silver DB, using Spark

# COMMAND ----------

updated_players_df = spark.table('silver.players')

# COMMAND ----------

display(updated_players_df)

# COMMAND ----------

# MAGIC %md
# MAGIC - Creating a Dataframe with a new column of the filtered current date, with the 'yyyy-MM-01' format

# COMMAND ----------

from pyspark.sql.functions import col, to_date, current_date, date_format

filtered_players_df = updated_players_df.filter(to_date(col('rating_date'), 'MMM/yyyy') == date_format(current_date(), 'yyyy-MM-01'))
display(filtered_players_df)

# COMMAND ----------

# MAGIC %md
# MAGIC - Checking if the current date filter are working

# COMMAND ----------

display(filtered_players_df.groupBy('rating_date').count())

# COMMAND ----------

filtered_players_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC - Saving the Dataframe as a table in the Silver DB

# COMMAND ----------

filtered_players_df.write.mode('overwrite').saveAsTable('silver.players_current_month')
