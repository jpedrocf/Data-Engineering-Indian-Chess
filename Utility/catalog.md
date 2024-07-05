**bronze.players_complete Catalog**
|Column Name|Type|Comment|
|--|--|--|
|fideid|int|A unique Federation ID of the player|
|name|string|Name of the player (last name, first name)|
|country|string|Nationality code of the player, country (3 characters)|
|sex|string|Sex of the player (M or F)|
|title|string|Official title of the player (GM - Grand Master, WGM - Woman Grand Master, IM - International Master, WIM - Woman International Master, FM - FIDE Master, WFM - Woman FIDE Master, CM - Candidate Master, WCM - Woman Candidate Master)|
|w_title|string|Title of the player (duplicated for women, a column to be removed during the ETL process)|
|o_title|string|Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)|
|foa_title|string|FOA title of the player (a column to be removed during the ETL process)|
|rating|int|Standard rating of the player|
|games|int|Number of standard non-online FIDE games played (a column to be removed during the ETL process)|
|k|double|K-factor for rating calculations (a column to be removed during the ETL process)|
|rapid_rating|int|Rapid rating of the player (a column to be removed during the ETL process)|
|rapid_games|int|Number of rapid games played (a column to be removed during the ETL process)|
|rapid_k|double|K-factor for rapid rating calculations (a column to be removed during the ETL process)|
|blitz_rating|int|Blitz rating of the player (a column to be removed during the ETL process)|
|blitz_games|int|Number of blitz games played (a column to be removed during the ETL process)|
|blitz_k|double|K-factor for blitz rating calculations (a column to be removed during the ETL process)|
|birthday|int|Year of birth of the player|
|flag|string|Flag of inactivity (I - inactive, WI - woman inactive, w - woman)|
|file_name|string|Name of the file from which data was collected|
|data_coleta|timestamp|Timestamp when the data was collected|

**bronze.event_games**
|Column Name|Type|Comment|
|--|--|--|
|id|int|Unique identifier for the match|
|event|string|Name of the event|
|site|string|Location of the event|
|date|date|Date of the match|
|round|int|Round number of the event|
|white|string|Name of the player with white pieces|
|black|string|Name of the player with black pieces|
|result|string|Result of the game (1-0 = white wins, 1/2 - 1/2 = draw, 0-1 = black wins)|
|white_title|string|Title of the player with white pieces|
|black_title|string|Title of the player with black pieces|
|white_elo|int|ELO rating of the player with white pieces|
|black_elo|int|ELO rating of the player with black pieces|
|eco|string|Encyclopedia of Chess Openings (ECO) code|
|opening|string|Name of the opening played|
|variation|string|Variation of the opening played|
|white_fide_id|int|FIDE ID of the player with white pieces|
|black_fide_id|int|FIDE ID of the player with black pieces|
|event_date|date|Date when the event took place|
|moves|string|Moves played in the game|


**silver.players Catalog**
|Column Name|Type|Comment|
|--|--|--|
|date_id_pk|string|Combination of Date and ID for a unique ID|
|rating_date|string|Date of the rating (MMM/yyyy)|
|fideid|int|A unique Federation ID of the player|
|name|string|Name of the player (last name, first name)|
|country|string|Nationality code of the player, country (3 characters)|
|sex|string|Sex of the player (M or F)|
|title|string|Official title of the player (GM - Grand Master, WGM - Woman Grand Master, IM - International Master, WIM - Woman International Master, FM - FIDE Master, WFM - Woman FIDE Master, CM - Candidate Master, WCM - Woman Candidate Master)|
|o_title|string|Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)|
|foa_title|string|FOA title of the player|
|rating|int|Standard rating of the player|
|birthday|int|Year of birth of the player|
|flag|string|Flag of inactivity (I - inactive, WI - woman inactive, w - woman)|
|file_name|string|Name of the file from which data was collected|
|data_coleta|timestamp|Timestamp when the data was collected|


**silver.players_current_month Catalog**
|Column Name|Type|Comment|
|--|--|--|
|date_id_pk|string|Combination of Date and ID for a unique ID|
|rating_date|string|Current date of the rating (MMM/yyyy)|
|fideid|int|A unique Federation ID of the player|
|name|string|Name of the player (last name, first name)|
|country|string|Nationality code of the player, country (3 characters)|
|sex|string|Sex of the player (M or F)|
|title|string|Official title of the player (GM - Grand Master, WGM - Woman Grand Master, IM - International Master, WIM - Woman International Master, FM - FIDE Master, WFM - Woman FIDE Master, CM - Candidate Master, WCM - Woman Candidate Master)|
|o_title|string|Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)|
|foa_title|string|FOA title of the player|
|rating|int|Standard rating of the player|
|birthday|int|Year of birth of the player|
|flag|string|Flag of inactivity (I - inactive, WI - woman inactive, w - woman)|
|file_name|string|Name of the file from which data was collected|
|data_coleta|timestamp|Timestamp when the data was collected|


**silver.players_female_base Catalog**
|Column Name|Type|Comment|
|--|--|--|
|date_id_pk|string|Combination of Date and ID for a unique ID|
|rating_date|string|Date of the rating (MMM/yyyy)|
|fideid|int|A unique Federation ID of the player|
|name|string|Name of the player (last name, first name)|
|country|string|Nationality code of the player, country (3 characters)|
|sex|string|Sex of the player (F)|
|title|string|Official title of the player (WGM - Woman Grand Master, WIM - Woman International Master, WFM - Woman FIDE Master, WCM - Woman Candidate Master)|
|o_title|string|Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)|
|foa_title|string|FOA title of the player|
|rating|int|Standard rating of the player|
|birthday|int|Year of birth of the player|
|flag|string|Flag of inactivity (WI - woman inactive, w - woman)|
|file_name|string|Name of the file from which data was collected|
|data_coleta|timestamp|Timestamp when the data was collected|

**silver.players_male_base Catalog**
|Column Name|Type|Comment|
|--|--|--|
|date_id_pk|string|Combination of Date and ID for a unique ID|
|rating_date|string|Current date of the rating (MMM/yyyy)|
|fideid|int|A unique Federation ID of the player|
|name|string|Name of the player (last name, first name)|
|country|string|Nationality code of the player, country (3 characters)|
|sex|string|Sex of the player (M or F)|
|title|string|Official title of the player (GM - Grand Master, IM - International Master, FM - FIDE Master, CM - Candidate Master)|
|o_title|string|Other titles of a player (IA - International Arbiter, FA - FIDE Arbiter, NA - National Arbiter, IO - International Organizer, FT - FIDE Trainer, FST - FIDE Senior Trainer, DI - Developmental Instructor, NI - National Instructor)|
|foa_title|string|FOA title of the player|
|rating|int|Standard rating of the player|
|birthday|int|Year of birth of the player|
|flag|string|Flag of inactivity (I - inactive)|
|file_name|string|Name of the file from which data was collected|
|data_coleta|timestamp|Timestamp when the data was collected|

%md
**gold.F_20_average_rating_by_country Catalog**
|Column Name|Type|Comment|
|--|--|--|
|date_id_pk|string|Federation, country, nationality (3 characters)|
|country|double|Average rating of the top 10 female players of each country|

**gold.F_2300_rated_players_per_country**
|Column Name|Type|Comment|
|--|--|--|
|country|string|Federation, country, nationality (3 characters)|
|player_count|int|Count of female players with a rating above 2300|


**gold.f_top10_average_rating_by_country**
|Column Name|Type|Comment|
|--|--|--|
|country|string|Federation, country, nationality (3 characters)|
|average_rating|float|Average rating of the top 10 female players of each country|


**gold.f_WGM_average_rating_by_country**
|Column Name|Type|Comment|
|--|--|--|
|country|string|Federation, country, nationality (3 characters)|
|average_rating|float|Average rating of the WGM players of each country|
|players|string|WGM title count|