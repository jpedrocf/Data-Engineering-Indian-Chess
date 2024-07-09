# Databricks notebook source
# MAGIC %md
# MAGIC - Checking the 'F' filter at sex

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from silver.players_current_month
# MAGIC where sex = 'F'

# COMMAND ----------

# MAGIC %md
# MAGIC - Creating a dataframe from the players_current_month table with the filter 'F' in sex to include only female players and then saving it as a new table in the silver layer

# COMMAND ----------

players_female_base = spark.table('silver.players_current_month').filter("sex = 'F'")
display(players_female_base)

# COMMAND ----------

display(players_female_base.groupBy('sex').count())

# COMMAND ----------

players_female_base.write.mode('overwrite').saveAsTable('silver.players_female_base')
