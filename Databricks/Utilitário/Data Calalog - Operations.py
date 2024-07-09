# Databricks notebook source
# MAGIC %md
# MAGIC - Adding comments to the columns (Data Catalog)

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN fideid COMMENT 'A unique Federation ID of the player';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN name COMMENT 'Name of the player (last name, first name)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN country COMMENT 'Nationality code of the player, country (3 characters)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN sex COMMENT 'Sex of the player (M or F)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN title COMMENT 'Official title of the player (GM - Grand Master, WGM - Woman Grand Master, IM - International Master, WIM - Woman International Master, FM - FIDE Master, WFM - Woman FIDE Master, CM - Candidate Master, WCM - Woman Candidate Master)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN w_title COMMENT 'Title of the player (duplicated for women, a column to be removed during the ETL process)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN o_title COMMENT 'Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN foa_title COMMENT 'FOA title of the player';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN rating COMMENT 'Standard rating of the player';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN games COMMENT 'Number of standard non-online FIDE games played (a column to be removed during the ETL process)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN k COMMENT 'K-factor for rating calculations (a column to be removed during the ETL process)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN rapid_rating COMMENT 'Rapid rating of the player (a column to be removed during the ETL process)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN rapid_games COMMENT 'Number of rapid games played (a column to be removed during the ETL process)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN rapid_k COMMENT 'K-factor for rapid rating calculations (a column to be removed during the ETL process)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN blitz_rating COMMENT 'Blitz rating of the player (a column to be removed during the ETL process)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN blitz_games COMMENT 'Number of blitz games played (a column to be removed during the ETL process)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN blitz_k COMMENT 'K-factor for blitz rating calculations (a column to be removed during the ETL process)';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN birthday COMMENT 'Year of birth of the player';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN flag COMMENT 'Flag of inactivity (I - inactive, WI - woman inactive, w - woman)';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN file_name COMMENT 'Name of the file from which data was collected';
# MAGIC
# MAGIC ALTER TABLE hive_metastore.bronze.players_complete 
# MAGIC ALTER COLUMN data_coleta COMMENT 'Timestamp when the data was collected';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN date_id_pk COMMENT 'Combination of Date and ID for a unique ID';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN rating_date COMMENT 'Date of the rating (MMM/yyyy)';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN fideid COMMENT 'A unique Federation ID of the player';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN name COMMENT 'Name of the player (last name, first name)';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN country COMMENT 'Nationality code of the player, country (3 characters)';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN sex COMMENT 'Sex of the player (M or F)';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN title COMMENT 'Official title of the player (GM - Grand Master, WGM - Woman Grand Master, IM - International Master, WIM - Woman International Master, FM - FIDE Master, WFM - Woman FIDE Master, CM - Candidate Master, WCM - Woman Candidate Master)';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN o_title COMMENT 'Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN foa_title COMMENT 'FOA title of the player';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN rating COMMENT 'Standard rating of the player';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN birthday COMMENT 'Year of birth of the player';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN flag COMMENT 'Flag of inactivity (I - inactive, WI - woman inactive, w - woman)';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN file_name COMMENT 'Name of the file from which data was collected';
# MAGIC
# MAGIC ALTER TABLE silver.players 
# MAGIC ALTER COLUMN data_coleta COMMENT 'Timestamp when the data was collected';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE silver.players_current_month
# MAGIC ALTER COLUMN rating_date COMMENT 'Current date of the rating (MMM/yyyy)'

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN id COMMENT 'Unique identifier for the match';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN event COMMENT 'Name of the event';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN site COMMENT 'Location of the event';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN date COMMENT 'Date of the match';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN round COMMENT 'Round number of the event';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN white COMMENT 'Name of the player with white pieces';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN black COMMENT 'Name of the player with black pieces';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN result COMMENT 'Result of the game (1-0 = white wins, 1/2 - 1/2 = draw, 0-1 = black wins)';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN white_title COMMENT 'Title of the player with white pieces';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN black_title COMMENT 'Title of the player with black pieces';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN white_elo COMMENT 'ELO rating of the player with white pieces';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN black_elo COMMENT 'ELO rating of the player with black pieces';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN eco COMMENT 'Encyclopedia of Chess Openings (ECO) code';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN opening COMMENT 'Name of the opening played';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN variation COMMENT 'Variation of the opening played';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN white_fide_id COMMENT 'FIDE ID of the player with white pieces';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN black_fide_id COMMENT 'FIDE ID of the player with black pieces';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN event_date COMMENT 'Date when the event took place';
# MAGIC ALTER TABLE bronze.event_games ALTER COLUMN moves COMMENT 'Moves played in the game';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE gold.F_20_average_rating_by_country ALTER COLUMN country COMMENT 'Federation, country, nationality (3 characters)';
# MAGIC ALTER TABLE gold.F_20_average_rating_by_country ALTER COLUMN average_rating COMMENT 'Average rating of the top 10 female players of each country';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE gold.F_2300_rated_players_per_country 
# MAGIC CHANGE COLUMN country COMMENT 'Federation, country, nationality (3 characters)';
# MAGIC
# MAGIC ALTER TABLE gold.F_2300_rated_players_per_country 
# MAGIC CHANGE COLUMN player_count COMMENT 'Count of female players with a rating above 2300';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE gold.f_top10_average_rating_by_country 
# MAGIC CHANGE COLUMN country COMMENT 'Federation, country, nationality (3 characters)';
# MAGIC
# MAGIC ALTER TABLE gold.f_top10_average_rating_by_country 
# MAGIC CHANGE COLUMN average_rating COMMENT 'Average rating of the top 10 female players of each country';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE gold.f_WGM_average_rating_by_country 
# MAGIC CHANGE COLUMN country COMMENT 'Federation, country, nationality (3 characters)';
# MAGIC
# MAGIC ALTER TABLE gold.f_WGM_average_rating_by_country
# MAGIC CHANGE COLUMN average_rating COMMENT 'Average rating of the WGM players of each country';
# MAGIC
# MAGIC ALTER TABLE gold.f_WGM_average_rating_by_country
# MAGIC CHANGE COLUMN players COMMENT 'WGM title count';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE gold.M_20_average_rating_by_country ALTER COLUMN country COMMENT 'Federation, country, nationality (3 characters)';
# MAGIC ALTER TABLE gold.M_20_average_rating_by_country ALTER COLUMN average_rating COMMENT 'Average rating of the top 10 male players of each country';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE gold.mix_IND_rank_evolution ALTER COLUMN country COMMENT 'Federation, country, nationality (3 characters), just IND';
# MAGIC ALTER TABLE gold.mix_IND_rank_evolution ALTER COLUMN rating_date COMMENT 'The reference date for the rating and ranking';
# MAGIC ALTER TABLE gold.mix_IND_rank_evolution ALTER COLUMN average_rating COMMENT 'Average rating of the top 10 players (male and female together) of IND';
# MAGIC ALTER TABLE gold.mix_IND_rank_evolution ALTER COLUMN rank COMMENT 'Ranking position for the reference month'

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE gold.mix_fed_rank_evolution ALTER COLUMN country COMMENT 'Federation, country, nationality (3 characters)';
# MAGIC ALTER TABLE gold.mix_fed_rank_evolution ALTER COLUMN rating_date COMMENT 'The reference date for the rating and ranking';
# MAGIC ALTER TABLE gold.mix_fed_rank_evolution ALTER COLUMN average_rating COMMENT 'Average rating of the top 10 players (male and female together) of each country';
# MAGIC ALTER TABLE gold.mix_fed_rank_evolution ALTER COLUMN rank COMMENT 'Ranking position for the reference month'

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE gold.IND_most_ef_openings ALTER COLUMN opening COMMENT 'Name of the opening (sequence of initial moves in chess)';
# MAGIC ALTER TABLE gold.IND_most_ef_openings ALTER COLUMN victory_count_ind COMMENT 'Victory count of the opening, for IND';
# MAGIC ALTER TABLE gold.IND_most_ef_openings ALTER COLUMN percentage_ind COMMENT 'Victory percentage of the opening, for IND';

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE gold.IND_world_comp_openings ALTER COLUMN opening COMMENT 'Name of the opening (sequence of initial moves in chess)';
# MAGIC ALTER TABLE gold.IND_world_comp_openings ALTER COLUMN victory_count_world COMMENT 'Victory count of the opening, for all players';
# MAGIC ALTER TABLE gold.IND_world_comp_openings ALTER COLUMN victory_count_ind COMMENT 'Victory count of the opening, for IND';
# MAGIC ALTER TABLE gold.IND_world_comp_openings ALTER COLUMN percentage_world COMMENT 'Victory percentage of the opening, for all players';
# MAGIC ALTER TABLE gold.IND_world_comp_openings ALTER COLUMN percentage_ind COMMENT 'Victory percentage of the opening, for IND';
