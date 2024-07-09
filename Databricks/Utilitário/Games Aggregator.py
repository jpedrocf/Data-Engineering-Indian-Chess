# Databricks notebook source
# MAGIC %md
# MAGIC # **Games Aggregator**

# COMMAND ----------

import pandas as pd
from sqlalchemy import create_engine
import pymysql
import re

# Connection settings
host = 'localhost'
user = 'root'
password = '12345'
database = 'db_xadrez'
table_name = 'games'
pgn_file_path = 'C:\internal_path'

# Function to parse PGN file
def parse_pgn(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    
    games = re.split(r'\n\n(?=\[)', data)
    parsed_games = []

    for game in games:
        lines = game.split('\n')
        game_data = {}
        moves = []

        for line in lines:
            if line.startswith('['):
                key, value = line[1:-1].split(' "', 1)
                game_data[key] = value[:-1]
            else:
                moves.append(line)

        game_data['Moves'] = ' '.join(moves).strip()
        parsed_games.append(game_data)
    
    return parsed_games

# Parse the PGN file
parsed_games = parse_pgn(pgn_file_path)

# Create DataFrame from parsed games
df = pd.DataFrame(parsed_games)

# Check the columns present in the DataFrame
print("Columns present in the DataFrame:")
print(df.columns)

# Rename columns to match the schema of the table in MySQL
expected_columns = [
    'Event', 'Site', 'Date', 'Round', 'White', 'Black', 'Result', 
    'WhiteTitle', 'BlackTitle', 'WhiteElo', 'BlackElo', 'ECO', 
    'Opening', 'Variation', 'WhiteFideId', 'BlackFideId', 'EventDate', 'Moves'
]

# Check if all expected columns are present
missing_columns = set(expected_columns) - set(df.columns)
if missing_columns:
    print(f"The following columns are missing from the DataFrame: {missing_columns}")
    for column in missing_columns:
        df[column] = None  # Add missing columns with None value

# Order the columns according to expected_columns
df = df[expected_columns]

# Verify the extracted data before inserting into the database
print("First rows of the DataFrame after renaming columns and filling missing values:")
print(df.head())

# Rename columns to match the names in the database
df.columns = [
    'event', 'site', 'date', 'round', 'white', 'black', 'result', 
    'white_title', 'black_title', 'white_elo', 'black_elo', 'eco', 
    'opening', 'variation', 'white_fide_id', 'black_fide_id', 'event_date', 'moves'
]

# Create the connection to the database using SQLAlchemy
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Insert the data into the 'games' table
df.to_sql(table_name, con=engine, if_exists='append', index=False)

print("Data successfully imported into the 'games' table in the 'db_xadrez' database.")

