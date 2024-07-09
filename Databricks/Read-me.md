# **MVP Project**
## 
## Introduction
This study focuses on examining the evolution of chess in India, aiming to provide a comprehensive overview of its development and current status. Over the years, India has produced numerous skilled chess players, contributing significantly to the global chess community. This research will delve into the historical progression and contemporary advancements of chess in India, highlighting key milestones and influential figures.

Additionally, the study will analyze the patterns and trends in chess openings favored by Indian players compared to those preferred globally. By investigating the strategies and techniques that have emerged from India, the research will offer insights into the unique aspects of Indian chess and its contributions to the broader chess landscape.

Through a detailed examination of these elements, this study seeks to understand India's role and impact in the world of chess, providing a nuanced perspective on its journey from historical roots to modern-day prominence.

## Workflow
To begin with this study, I gathered data from the [FIDE website](https://www.fide.com/), which is the International Chess Federation, and from the daily chess newspaper called "[The Week in Chess](https://theweekinchess.com/twic)".

On the FIDE platform, I downloaded 113 files related to chess players for the period from February 2015 to June 2024. Among these data are the personal ID of each player (FIDE ID), the player's name, nationality, gender, titles won, ratings, year of birth, and a flag indicating whether the player is active or inactive. The files, when downloaded, had a standard name, where from index 9 to 14 contained the month and year corresponding to the table. All files were in XML format. To optimize, I created an [XML to Parquet converter](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/Utilit%C3%A1rio/XML%20to%20parquet.gzip.py) that read all the files saved in the folder and converted them to Parquet into a single table. This same code also created two new columns, one containing the name of the file itself and another containing the download date.

The "The Week in Chess" platform provided me with recent championship data played by the best players in the world, containing information such as the name and location of the championship, date, round, player with white pieces, player with black pieces, result, title of the white player, title of the black player, ranking of the white player, ranking of the black player, opening played, FIDE ID of each player, and the date of the event.

These data were processed by a [Python script that aggregated all the files saved in a internal folder into a single table](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/Utilit%C3%A1rio/Games%20Aggregator.py). I also added a unique identifier for each match.

After merging the match and player files, I uploaded the tables to Databricks and placed them in internally [created schemas](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/Utilit%C3%A1rio/create%20schema.py). The schemas I created were Bronze, Silver, and Gold to use the layered data architecture (medallion).

Both the matches and the players were placed in the Bronze schema to go through the ETL process.

At this point, I used Databricks notebooks to perform checks and cleanups, describing the step-by-step process in each of them.

After performing the ETL process, I saved the created DataFrame in the Silver database, where I did more thorough column cleaning, data filtering, and table merging, to save it in the Gold database.

After creating all the tables, I made a [data catalog](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/Utilit%C3%A1rio/Data%20Catalog.md) in markdown format, using SQL to comment on the tables and also did a [Pipeline](https://imgur.com/BocNZzN) (also did a [JSON version](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/Utilit%C3%A1rio/Pipeline%20-%20JSON.json)) to automatic update all tables, everytime i input new data.


## Questions

- **Is India a chess powerhouse?**

Looking at players under 20 years old (promising players) by federation, we have this result for [male](https://imgur.com/kUMp0ee) and [female](https://imgur.com/1qmfPU6) categories, with India being the leading federation in both, having the highest average rating. Here we can see the notebooks about each one [Male under 20](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Male/silver%20to%20gold%20-%20%3C20%20avg.%20rating.py) and [Female under 20](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Female/silver%20to%20gold%20-%20%3C20%20avg.%20rating.py).

Looking at highly ranked players with high ratings (male >2600 and female >2300), we have this result for both [male](https://imgur.com/W9u4KnM) and [female](https://imgur.com/QoR6wLJ) categories, with India being the second federation with the highest number of players in these conditions. Here we can see the notebooks about each one [Male >2600 rating](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Male/silver%20to%20gold%20-%20%3E2600%20rating%20count.py) and [Female >2300 rating](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Female/silver%20to%20gold%20-%20%3E2300%20rating%20count.py).

Looking at players with the title of [GM (male)](https://imgur.com/kKqGbYa) and [WGM (female)](https://imgur.com/ucmhk6k), we can observe that India is the third federation with the most GMs and WGMs (tied with Germany for WGMs), and it also has the highest average rating among the top 10 countries with the most active GMs. Here we can see the notebooks about each one [Male GM Count](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Male/silver%20to%20gold%20-%20count%20GM%20avg.%20rating.py) and [Female WGM Count](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Female/silver%20to%20gold%20-%20WGM%20count%20avg.%20rating.py)

Looking at the [male](https://imgur.com/oLalrHg) and [female](https://imgur.com/TdzqdlN) federation rankings, following the FIDE criteria (average current rating of the top 10 active players per federation), we have India occupying the second position in both male and female categories. Here we can see the notebooks about each one [Federations Rank Male](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Male/silver%20to%20gold%20-%20fed%20avg.%20rating.py) and [Federations Rank Female](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Female/silver%20to%20gold%20-%20fed%20avg.%20rating.py)

- **Is there an evolution in Indian chess?**

Here is a [visualization of India's position](https://imgur.com/G1nl3Ts) evolution in the federations ranking, where the country has held its best historical position (second place) since February 2023. Here we can see the [notebook of the data cleaning and filtering](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/FIDE%20-%20Players/Mix/silver%20to%20gold%20-%20fed%20ranking%20evolution%20by%20time.ipynb)

- **What are the most successful openings in Indian chess compared to the rest of the world?**

When filtering for openings with over 100 wins to ensure a more reliable sample, and [comparing the average win percentage of the world versus India](https://imgur.com/xweIQlL), we find that out of 11 openings, India surpasses the global average in 7 of them. Here we can see the [notebook used to do the comparision, cleaning and filtering](https://github.com/jpedrocf/ProjetoMVPBancodeDados/blob/main/Databricks/2.%20Silver%20to%20Gold/TWIC%20-%20Games/silver%20to%20gold%20-%20matchs%20common%20openings.ipynb)

## Conclusion

Based on the data and analysis from various perspectives, it is clear that India is a chess powerhouse and has demonstrated significant growth in recent years. India leads in the average ratings of players under 20 years old for both male and female categories, indicating a strong future with many promising young players. When considering highly ranked players, India stands out as the second federation with the most male players rated above 2600 and female players rated above 2300, showing depth in top-tier talent.

India's status as a chess powerhouse is further solidified by its ranking as the third federation with the most Grandmasters (GMs) and Women Grandmasters (WGMs), tied with Germany for WGMs. Notably, Indian GMs boast the highest average rating among the top 10 countries, underscoring the quality of its elite players.

In terms of federation rankings, India holds the second position for both male and female categories according to FIDE criteria, reflecting the consistent strength of its players. This impressive ranking has been maintained since February 2023, marking India's best historical position.

Moreover, when analyzing successful chess openings, Indian players perform better than the global average in the majority of commonly used openings. This suggests a strategic edge and effective preparation in their games.

Overall, the comprehensive data and trends confirm that India is not only a leading force in the chess world but also continues to progress, with a bright future ahead in the sport.
