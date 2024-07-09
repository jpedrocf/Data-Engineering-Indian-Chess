# Databricks notebook source
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS hive_metastore.gold.india_rank_per_month

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS hive_metastore.gold.average_rating_by_country

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC ALTER TABLE hive_metastore.gold.average_rating_by_country RENAME TO hive_metastore.gold.MIX_avg_rating_by_country;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC ALTER TABLE hive_metastore.gold.20_average_rating_by_country RENAME TO hive_metastore.gold.MIX_20_average_rating_by_country;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC ALTER TABLE hive_metastore.gold.2600_rapid_rated_players_per_country RENAME TO hive_metastore.gold.MIX_2600_rapid_rated_players_per_country;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC ALTER TABLE hive_metastore.gold.2600_rated_players_per_country RENAME TO hive_metastore.gold.MIX_2600_rated_players_per_country;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC ALTER TABLE hive_metastore.gold.f20_average_rating_by_country RENAME TO hive_metastore.gold.F_20_average_rating_by_country;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC ALTER TABLE hive_metastore.gold.gm_average_rating_by_country RENAME TO hive_metastore.gold.MIX_gm_average_rating_by_country;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC ALTER TABLE hive_metastore.gold.gms_by_country RENAME TO hive_metastore.gold.MIX_gms_by_country;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS hive_metastore.silver.partidas_campeonato

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE hive_metastore.bronze.partidas_campeonato RENAME to hive_metastore.bronze.event_games;

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists hive_metastore.gold.ind_most_ef_openings

# COMMAND ----------

# MAGIC %sql
# MAGIC alter table hive_metastore.gold.mix_gm_average_rating_by_country RENAME to hive_metastore.gold.mix_gm_count_and_average_rating_by_country

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists hive_metastore.silver.players_male_base

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists hive_metastore.default.partidas_campeonato
