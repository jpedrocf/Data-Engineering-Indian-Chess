# Databricks notebook source
# MAGIC %md
# MAGIC **bronze.players_complete Catalog**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |fideid|int|A unique Federation ID of the player|
# MAGIC |name|string|Name of the player (last name, first name)|
# MAGIC |country|string|Nationality code of the player, country (3 characters)|
# MAGIC |sex|string|Sex of the player (M or F)|
# MAGIC |title|string|Official title of the player (GM - Grand Master, WGM - Woman Grand Master, IM - International Master, WIM - Woman International Master, FM - FIDE Master, WFM - Woman FIDE Master, CM - Candidate Master, WCM - Woman Candidate Master)|
# MAGIC |w_title|string|Title of the player (duplicated for women, a column to be removed during the ETL process)|
# MAGIC |o_title|string|Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)|
# MAGIC |foa_title|string|FOA title of the player (a column to be removed during the ETL process)|
# MAGIC |rating|int|Standard rating of the player|
# MAGIC |games|int|Number of standard non-online FIDE games played (a column to be removed during the ETL process)|
# MAGIC |k|double|K-factor for rating calculations (a column to be removed during the ETL process)|
# MAGIC |rapid_rating|int|Rapid rating of the player (a column to be removed during the ETL process)|
# MAGIC |rapid_games|int|Number of rapid games played (a column to be removed during the ETL process)|
# MAGIC |rapid_k|double|K-factor for rapid rating calculations (a column to be removed during the ETL process)|
# MAGIC |blitz_rating|int|Blitz rating of the player (a column to be removed during the ETL process)|
# MAGIC |blitz_games|int|Number of blitz games played (a column to be removed during the ETL process)|
# MAGIC |blitz_k|double|K-factor for blitz rating calculations (a column to be removed during the ETL process)|
# MAGIC |birthday|int|Year of birth of the player|
# MAGIC |flag|string|Flag of inactivity (I - inactive, WI - woman inactive, w - woman)|
# MAGIC |file_name|string|Name of the file from which data was collected|
# MAGIC |data_coleta|timestamp|Timestamp when the data was collected|

# COMMAND ----------

# MAGIC %md
# MAGIC ## **silver.players Catalog**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |date_id_pk|string|Combination of Date and ID for a unique ID|
# MAGIC |rating_date|string|Date of the rating (MMM/yyyy)|
# MAGIC |fideid|int|A unique Federation ID of the player|
# MAGIC |name|string|Name of the player (last name, first name)|
# MAGIC |country|string|Nationality code of the player, country (3 characters)|
# MAGIC |sex|string|Sex of the player (M or F)|
# MAGIC |title|string|Official title of the player (GM - Grand Master, WGM - Woman Grand Master, IM - International Master, WIM - Woman International Master, FM - FIDE Master, WFM - Woman FIDE Master, CM - Candidate Master, WCM - Woman Candidate Master)|
# MAGIC |o_title|string|Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)|
# MAGIC |foa_title|string|FOA title of the player|
# MAGIC |rating|int|Standard rating of the player|
# MAGIC |birthday|int|Year of birth of the player|
# MAGIC |flag|string|Flag of inactivity (I - inactive, WI - woman inactive, w - woman)|
# MAGIC |file_name|string|Name of the file from which data was collected|
# MAGIC |data_coleta|timestamp|Timestamp when the data was collected|
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **silver.players_current_month Catalog**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |date_id_pk|string|Combination of Date and ID for a unique ID|
# MAGIC |rating_date|string|Current date of the rating (MMM/yyyy)|
# MAGIC |fideid|int|A unique Federation ID of the player|
# MAGIC |name|string|Name of the player (last name, first name)|
# MAGIC |country|string|Nationality code of the player, country (3 characters)|
# MAGIC |sex|string|Sex of the player (M or F)|
# MAGIC |title|string|Official title of the player (GM - Grand Master, WGM - Woman Grand Master, IM - International Master, WIM - Woman International Master, FM - FIDE Master, WFM - Woman FIDE Master, CM - Candidate Master, WCM - Woman Candidate Master)|
# MAGIC |o_title|string|Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)|
# MAGIC |foa_title|string|FOA title of the player|
# MAGIC |rating|int|Standard rating of the player|
# MAGIC |birthday|int|Year of birth of the player|
# MAGIC |flag|string|Flag of inactivity (I - inactive, WI - woman inactive, w - woman)|
# MAGIC |file_name|string|Name of the file from which data was collected|
# MAGIC |data_coleta|timestamp|Timestamp when the data was collected|
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Bronze Table: Event Games**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |id|int|Unique identifier for the match|
# MAGIC |event|string|Name of the event|
# MAGIC |site|string|Location of the event|
# MAGIC |date|date|Date of the match|
# MAGIC |round|int|Round number of the event|
# MAGIC |white|string|Name of the player with white pieces|
# MAGIC |black|string|Name of the player with black pieces|
# MAGIC |result|string|Result of the game (1-0 = white wins, 1/2 - 1/2 = draw, 0-1 = black wins)|
# MAGIC |white_title|string|Title of the player with white pieces|
# MAGIC |black_title|string|Title of the player with black pieces|
# MAGIC |white_elo|int|ELO rating of the player with white pieces|
# MAGIC |black_elo|int|ELO rating of the player with black pieces|
# MAGIC |eco|string|Encyclopedia of Chess Openings (ECO) code|
# MAGIC |opening|string|Name of the opening played|
# MAGIC |variation|string|Variation of the opening played|
# MAGIC |white_fide_id|int|FIDE ID of the player with white pieces|
# MAGIC |black_fide_id|int|FIDE ID of the player with black pieces|
# MAGIC |event_date|date|Date when the event took place|
# MAGIC |moves|string|Moves played in the game|
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **silver.players_female_base Catalog**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |date_id_pk|string|Combination of Date and ID for a unique ID|
# MAGIC |rating_date|string|Date of the rating (MMM/yyyy)|
# MAGIC |fideid|int|A unique Federation ID of the player|
# MAGIC |name|string|Name of the player (last name, first name)|
# MAGIC |country|string|Nationality code of the player, country (3 characters)|
# MAGIC |sex|string|Sex of the player (F)|
# MAGIC |title|string|Official title of the player (WGM - Woman Grand Master, WIM - Woman International Master, WFM - Woman FIDE Master, WCM - Woman Candidate Master)|
# MAGIC |o_title|string|Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)|
# MAGIC |foa_title|string|FOA title of the player|
# MAGIC |rating|int|Standard rating of the player|
# MAGIC |birthday|int|Year of birth of the player|
# MAGIC |flag|string|Flag of inactivity (WI - woman inactive, w - woman)|
# MAGIC |file_name|string|Name of the file from which data was collected|
# MAGIC |data_coleta|timestamp|Timestamp when the data was collected|

# COMMAND ----------

# MAGIC %md
# MAGIC **silver.players_male_base Catalog**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |date_id_pk|string|Combination of Date and ID for a unique ID|
# MAGIC |rating_date|string|Current date of the rating (MMM/yyyy)|
# MAGIC |fideid|int|A unique Federation ID of the player|
# MAGIC |name|string|Name of the player (last name, first name)|
# MAGIC |country|string|Nationality code of the player, country (3 characters)|
# MAGIC |sex|string|Sex of the player (M or F)|
# MAGIC |title|string|Official title of the player (GM - Grand Master, IM - International Master, FM - FIDE Master, CM - Candidate Master)|
# MAGIC |o_title|string|Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)|
# MAGIC |foa_title|string|FOA title of the player|
# MAGIC |rating|int|Standard rating of the player|
# MAGIC |birthday|int|Year of birth of the player|
# MAGIC |flag|string|Flag of inactivity (I - inactive)|
# MAGIC |file_name|string|Name of the file from which data was collected|
# MAGIC |data_coleta|timestamp|Timestamp when the data was collected|

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.F_20_average_rating_by_country Catalog**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |date_id_pk|string|Federation, country, nationality (3 characters)|
# MAGIC |country|double|Average rating of the top 10 female players of each country, in the current month|

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.F_2300_rated_players_per_country**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |country|string|Federation, country, nationality (3 characters)|
# MAGIC |player_count|int|Count of female players with a rating above 2300, in the current month|

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.f_top10_average_rating_by_country**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |country|string|Federation, country, nationality (3 characters)|
# MAGIC |average_rating|float|Average rating of the top 10 female players of each country, in the current month|

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.f_WGM_average_rating_by_country**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |country|string|Federation, country, nationality (3 characters)|
# MAGIC |average_rating|float|Average rating of the WGM players of each country, in the current month|
# MAGIC |players|string|WGM title count of active players (flag == null)|
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.M_20_average_rating_by_country Catalog**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |date_id_pk|string|Federation, country, nationality (3 characters)|
# MAGIC |country|double|Average rating of the top 10 male players of each country, in the current month|

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.M_2600_rated_players_per_country**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |country|string|Federation, country, nationality (3 characters)|
# MAGIC |player_count|int|Count of male players with a rating above 2600, in the current month of active players (flag == null)|

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.M_GM_average_rating_by_country**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |country|string|Federation, country, nationality (3 characters)|
# MAGIC |average_rating|float|Average rating of the GM players of each country, in the current month|
# MAGIC |players|string|GM title count of active players (flag == null)|
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.M_top10_average_rating_by_country**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |country|string|Federation, country, nationality (3 characters)|
# MAGIC |average_rating|float|Average rating of the top 10 male players of each country, in the current month|

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.mix_fed_rank_evolution**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |country|string|Federation, country, nationality (3 characters)|
# MAGIC |rating_date|date|The reference date for the rating and ranking|
# MAGIC |average_rating|double|Average rating of the top 10 players (male and female together) of each country|
# MAGIC |rank|int|Ranking position for the reference month|

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.mix_IND_rank_evolution**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |country|string|Federation, country, nationality (3 characters), just IND|
# MAGIC |rating_date|date|The reference date for the rating and ranking|
# MAGIC |average_rating|double|Average rating of the top 10 players (male and female together) of IND|
# MAGIC |rank|int|Ranking position for the reference month|

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.IND_most_ef_openings**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |opening|string|Name of the opening (sequence of initial moves in chess)|
# MAGIC |victory_count_ind|int|Victory count of the opening, for IND|
# MAGIC |percentage_ind|double|Victory percentage of the opening, for IND|

# COMMAND ----------

# MAGIC %md
# MAGIC **gold.IND_world_comp_openings**
# MAGIC |Column Name|Type|Comment|
# MAGIC |--|--|--|
# MAGIC |opening|string|Name of the opening (sequence of initial moves in chess)|
# MAGIC |victory_count_world|int|Victory count of the opening, for all players|
# MAGIC |victory_count_ind|int|Victory count of the opening, for IND|
# MAGIC |percentage_world|double|Victory percentage of the opening, for all players|
# MAGIC |percentage_ind|double|Victory percentage of the opening, for IND|
