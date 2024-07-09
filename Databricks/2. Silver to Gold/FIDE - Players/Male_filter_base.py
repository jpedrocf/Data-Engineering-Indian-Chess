# Databricks notebook source
# MAGIC %md
# MAGIC - Checking the 'M' filter at sex

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from silver.players_current_month
# MAGIC where sex = 'M'

# COMMAND ----------

# MAGIC %md
# MAGIC - Creating a dataframe from the players_current_month table with the filter 'M' in sex to include only male players and then saving it as a new table in the silver layer

# COMMAND ----------

players_male_base = spark.table('silver.players_current_month').filter("sex = 'M'")
display(players_male_base)

# COMMAND ----------

display(players_male_base.groupBy('sex').count())

# COMMAND ----------

players_male_base.write.mode('overwrite').saveAsTable('silver.players_male_base')
