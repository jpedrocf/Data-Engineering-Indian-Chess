# Databricks notebook source
# MAGIC %md
# MAGIC # **Players Table Root**

# COMMAND ----------

# MAGIC %md
# MAGIC - Creating a backup of the players table

# COMMAND ----------

players_complete_bckup = spark.table('bronze.players_complete')
players_complete_bckup.write.mode('overwrite').saveAsTable('bronze.players_complete_bckup')

# COMMAND ----------

# MAGIC %md
# MAGIC - Dataframe creation and update of the table players_complete in the bronze DB, using Spark

# COMMAND ----------

players_default = spark.table('current_month_players')

# COMMAND ----------

from pyspark.sql.functions import *
filename_current = players_default.agg(first(col('file_name'))).collect()[0][0]
print(filename_current)

# COMMAND ----------

players_df = spark.table('bronze.players_complete')

# COMMAND ----------

# MAGIC %md
# MAGIC - Performing a conditional check to avoid appending duplicate data

# COMMAND ----------

players_df_checker = players_df.filter(col('file_name').isin(filename_current))
if players_df_checker.isEmpty():
    players_default.write.mode('append').saveAsTable('bronze.players_complete')
    print('players_complete appended')
else:
    print('File_name already exists.')

players_df = spark.table('bronze.players_complete')

# COMMAND ----------

# MAGIC %md
# MAGIC - Creating a function in Spark to extract and store the characters from indices 9 to 14 to create a new column with these stored characters, which will be my date column. This was only possible because all files came standardized with the month and year in these indices.

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.functions import StringType

# Function to extract characters from indices 9 to 14

extract_substring = F.udf(lambda x: x[9:14] if len(x) > 15 else x, StringType())

# Apply the transformation to the column file_name
players_df_updated = players_df.withColumn('rating_date', extract_substring(F.col('file_name')))

# Display the result
display(players_df_updated)



# COMMAND ----------

# MAGIC %md
# MAGIC - Checking the created column

# COMMAND ----------

display(players_df_updated.groupBy('rating_date').count())

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *
import datetime

# COMMAND ----------

players_df_updated.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC - Filtering and transforming data, focusing on converting columns to appropriate types and formatting dates for analysis or display

# COMMAND ----------

from pyspark.sql.functions import col, date_format

players_transform_type = players_df_updated.filter(col('fideid').isNotNull()) \
    .withColumn('fideid', col('fideid').cast('integer')) \
    .withColumn('rating_date', to_date(col('rating_date'), 'MMMyy')) \
    .withColumn('birthday', col('birthday').cast('integer')) \
    .withColumn('rating', col('rating').cast('integer'))

players_transform_type.printSchema()
display(players_transform_type)

# COMMAND ----------

# MAGIC %md
# MAGIC - Changing the date format

# COMMAND ----------

from pyspark.sql.functions import date_format

players_transform_type = players_transform_type.withColumn('rating_date', date_format(col('rating_date'), 'MMM/yyyy'))

display(players_transform_type)

# COMMAND ----------

# MAGIC %md
# MAGIC - Checking the length of entries in the country and sex columns and excluding anomalies

# COMMAND ----------

if players_transform_type.filter(length('country') != 3).isEmpty():
    print('All countries checked, with no errors')
    
else:
    players_transform_type = players_transform_type.filter(length('country') == 3)
    players_errors = players_transform_type.filter(length('country') != 3).count()
    print(f'There was {players_errors} errors.')
    


# COMMAND ----------

if players_transform_type.filter(length('sex') != 1).isEmpty():
    print('All rows checked, with no errors')
    
else:
    players_transform_type = players_transform_type.filter(length('sex') == 1)
    players_errors = players_transform_type.filter(length('sex') != 1).count()
    print(f'There was {players_errors} errors.')
    

# COMMAND ----------

# MAGIC %md
# MAGIC - Checking if when sex = F it represents a male title, while counting and replacing the errors

# COMMAND ----------

# DBTITLE 1,CORRECTING TITLES - FEMALE
from pyspark.sql.functions import col, when, udf
from pyspark.sql.types import IntegerType

# Initialize a counter
substitution_counter = spark.sparkContext.accumulator(0)

# Define a UDF to count the substitutions
def count_substitution(title, sex):
    global substitution_counter
    if sex == 'F' and title in ['GM', 'IM', 'FM', 'CM']:
        substitution_counter.add(1)
    return title

count_substitution_udf = udf(count_substitution, StringType())

# Apply the substitutions and count
players_transform_type2 = players_transform_type.withColumn(
    'title',
    when((col('sex') == 'F') & (col('title') == 'GM'), 'WGM')
    .when((col('sex') == 'F') & (col('title') == 'IM'), 'WIM')
    .when((col('sex') == 'F') & (col('title') == 'FM'), 'WFM')
    .when((col('sex') == 'F') & (col('title') == 'CM'), 'WCM')
    .otherwise(col('title'))
)

# Apply the UDF to count the substitutions
players_transform_type3 = players_transform_type2.withColumn(
    'title', count_substitution_udf(col('title'), col('sex'))
)

# Print the substitution counter
print(f"Substitution counter = {substitution_counter.value}")

# COMMAND ----------

# MAGIC %md
# MAGIC - Checking if when sex = M it represents a female title, while counting and replacing the errors

# COMMAND ----------

# DBTITLE 1,CORRECTING TITLES - MALE
from pyspark.sql.functions import col, when, udf
from pyspark.sql.types import IntegerType

# Initialize a counter
substitution_counter2 = spark.sparkContext.accumulator(0)

# Define a UDF to count the substitutions
def count_substitution(title, sex):
    global substitution_counter2
    if sex == 'M' and title in ['WGM', 'WIM', 'WFM', 'WCM']:
        substitution_counter2.add(1)
    return title

count_substitution_udf2 = udf(count_substitution, StringType())

# Apply the substitutions and count
players_transform_type3 = players_transform_type3.withColumn(
    'title',
    when((col('sex') == 'M') & (col('title') == 'WGM'), 'GM')
    .when((col('sex') == 'M') & (col('title') == 'WIM'), 'IM')
    .when((col('sex') == 'M') & (col('title') == 'WFM'), 'FM')
    .when((col('sex') == 'M') & (col('title') == 'WCM'), 'CM')
    .otherwise(col('title'))
)

# Apply the UDF to count the substitutions
players_transform_type4 = players_transform_type3.withColumn(
    'title', count_substitution_udf2(col('title'), col('sex'))
)

# Print the substitution counter
print(f"Substitution counter = {substitution_counter2.value}")

# COMMAND ----------

# MAGIC %md
# MAGIC - Checking the flags with the sex

# COMMAND ----------

# DBTITLE 1,CORRECTING FLAGS - FEMALE
from pyspark.sql.functions import col, when, udf
from pyspark.sql.types import StringType

substitution_counter_flag = spark.sparkContext.accumulator(0)

def count_flag_substitution(flag, sex):
    global substitution_counter_flag
    if sex == 'F' and flag == 'I':
        substitution_counter_flag.add(1)
        return 'WI'
    return flag

count_flag_substitution_udf = udf(count_flag_substitution, StringType())


players_transform_flag = players_transform_type4.withColumn(
    'flag', count_flag_substitution_udf(col('flag'), col('sex'))
)


print(f"Substitution counter = {substitution_counter_flag.value}")

# COMMAND ----------

# DBTITLE 1,CORRECTING FLAGS - MALE
from pyspark.sql.functions import col, when, udf
from pyspark.sql.types import StringType

substitution_counter_flag = spark.sparkContext.accumulator(0)

def count_flag_substitution(flag, sex):
    global substitution_counter_flag
    if sex == 'M' and flag == 'WI':
        substitution_counter_flag.add(1)
        return 'I'
    return flag

count_flag_substitution_udf = udf(count_flag_substitution, StringType())


players_transform_flag = players_transform_type.withColumn(
    'flag', count_flag_substitution_udf(col('flag'), col('sex'))
)


print(f"Substitution counter = {substitution_counter_flag.value}")

# COMMAND ----------

# MAGIC %md
# MAGIC - Reordering the columns

# COMMAND ----------

# Reorder the columns to place the last column as the first column
columns = players_transform_flag.columns
reordered_columns = [columns[-1]] + columns[:-1]

# Select the columns in the new order
players_transform_flag_reordered = players_transform_flag.select(reordered_columns)

display(players_transform_flag_reordered)

# COMMAND ----------

# MAGIC %md
# MAGIC - Creating a new column by concatenating 'rating_date' ande 'fideid', for a unique ID

# COMMAND ----------

from pyspark.sql.functions import concat_ws

# Create a new column by concatenating 'rating_date' and 'fideid'
players_transform_flag_reordered = players_transform_flag_reordered.withColumn('date_id_pk', concat_ws('_', 'rating_date', 'fideid'))

# Reorder the columns to place the new column as the first column
columns = players_transform_flag_reordered.columns
reordered_columns = ['date_id_pk'] + columns[:-1]

# Select the columns in the new order
players_final = players_transform_flag_reordered.select(reordered_columns)

display(players_final)

# COMMAND ----------

# MAGIC %md
# MAGIC - Cleaning the non-usable columns

# COMMAND ----------

# Drop the specified columns from the DataFrame
columns_to_drop = ['w_title', 'games', 'k', 'rapid_rating', 'rapid_games', 'rapid_k', 'blitz_rating', 'blitz_games', 'blitz_k', 'rating_date_fideid']
players_final2 = players_final.drop(*columns_to_drop)

display(players_final2)

# COMMAND ----------

# MAGIC %md
# MAGIC - Transforming the date format

# COMMAND ----------

from pyspark.sql.functions import date_format

# Transform the 'rating_date' column to date format and then format it as 'MMM/yyyy'
players_final2 = players_final2.withColumn('rating_date', date_format(to_date('rating_date', 'MMM/yyyy'), 'MMM/yyyy'))

display(players_final2)

# COMMAND ----------

# MAGIC %md
# MAGIC - Overwriting the players table in the silver's DB

# COMMAND ----------

players_final2.write.mode('overwrite').saveAsTable('silver.players')
