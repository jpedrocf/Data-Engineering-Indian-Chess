# **MVP Project**
## 
## The objective of this MVP is to check the evolution of chess in India.
## The questions I want to answer are:

- **Is India a chess powerhouse?**
- **Is there an evolution in Indian chess?**
- **What are the most successful openings in Indian chess compared to the rest of the world?**

To answer these questions, I gathered data from the [FIDE website](https://www.fide.com/), which is the International Chess Federation, and from the daily chess newspaper called "[The Week in Chess](https://theweekinchess.com/twic)".

On the FIDE platform, I downloaded 113 files related to chess players for the period from February 2015 to June 2024. Among these data are the personal ID of each player (FIDE ID), the player's name, nationality, gender, titles won, ratings, year of birth, and a flag indicating whether the player is active or inactive. The files, when downloaded, had a standard name, where from index 9 to 14 contained the month and year corresponding to the table. All files were in XML format. To optimize, I created an [XML to Parquet converter](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/Utilit%C3%A1rio/XML%20to%20parquet.gzip.py) that read all the files saved in the folder and converted them to Parquet into a single table. This same code also created two new columns, one containing the name of the file itself and another containing the download date.

The "The Week in Chess" platform provided me with recent championship data played by the best players in the world, containing information such as the name and location of the championship, date, round, player with white pieces, player with black pieces, result, title of the white player, title of the black player, ranking of the white player, ranking of the black player, opening played, FIDE ID of each player, and the date of the event.

These data were processed by a [Python script that aggregated all the files saved in a internal folder into a single table](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/Utilit%C3%A1rio/Games%20Aggregator.py). I also added a unique identifier for each match.

After merging the match and player files, I uploaded the tables to Databricks and placed them in internally [created schemas](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/Utilit%C3%A1rio/create%20schema.py). The schemas I created were Bronze, Silver, and Gold to use the layered data architecture (medallion).

Both the matches and the players were placed in the Bronze schema to go through the ETL process.

At this point, I used Databricks notebooks to perform checks and cleanups, describing the step-by-step process in each of them.

After performing the ETL process, I saved the created DataFrame in the Silver database, where I did more thorough column cleaning, data filtering, and table merging, to save it in the Gold database.

After creating all the tables, I made a [data catalog](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/Utilit%C3%A1rio/Data%20Catalog.md) in markdown format, using SQL to comment on the tables and also did a [Pipeline](https://imgur.com/BocNZzN) (also did a [JSON version](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/Utilit%C3%A1rio/Pipeline%20-%20JSON.json)) to automatic update all tables, everytime i input new data.

With the tables created in the Gold database, I answer the questions posed at the beginning of this MVP.

- **Is India a chess powerhouse?**

Looking at players under 20 years old (promising players) by federation, we have this result for [male](https://imgur.com/kUMp0ee) and [female](https://imgur.com/1qmfPU6) categories, with India being the leading federation in both, having the highest average rating. Here we can see the notebooks about each one [Male under 20](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Male/silver%20to%20gold%20-%20%3C20%20avg.%20rating.py) and [Female under 20](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Female/silver%20to%20gold%20-%20%3C20%20avg.%20rating.py)







- **Is there an evolution in Indian chess?**

  
- **What are the most successful openings in Indian chess compared to the rest of the world?**
