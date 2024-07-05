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
