# Databricks notebook source
# MAGIC %md
# MAGIC # **Internal code that transforms an entire folder of XML files into a single parquet.gzip file**

# COMMAND ----------

import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime
import os

xml_file_path = r'C:\Users\internal_path...'
file_names = []
df = pd.DataFrame()

for file_name in os.listdir(xml_file_path):
    file_path = os.path.join(xml_file_path, file_name)

    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()
        print("XML parsed successfully")
    except Exception as e:
        print(f"Error parsing XML: {e}")

    # Initialize a list to store the data
    data = []

    # Iterate over each <player> element in the XML
    for player in root.findall('player'):
        try:
            player_data = {
                'fideid': player.find('fideid').text if player.find('fideid') is not None else None,
                'name': player.find('name').text if player.find('name') is not None else None,
                'country': player.find('country').text if player.find('country') is not None else None,
                'sex': player.find('sex').text if player.find('sex') is not None else None,
                'title': player.find('title').text if player.find('title') is not None else None,
                'w_title': player.find('w_title').text if player.find('w_title') is not None else None,
                'o_title': player.find('o_title').text if player.find('o_title') is not None else None,
                'foa_title': player.find('foa_title').text if player.find('foa_title') is not None else None,
                'rating': player.find('rating').text if player.find('rating') is not None else None,
                'games': player.find('games').text if player.find('games') is not None else None,
                'k': player.find('k').text if player.find('k') is not None else None,
                'rapid_rating': player.find('rapid_rating').text if player.find('rapid_rating') is not None else None,
                'rapid_games': player.find('rapid_games').text if player.find('rapid_games') is not None else None,
                'rapid_k': player.find('rapid_k').text if player.find('rapid_k') is not None else None,
                'blitz_rating': player.find('blitz_rating').text if player.find('blitz_rating') is not None else None,
                'blitz_games': player.find('blitz_games').text if player.find('blitz_games') is not None else None,
                'blitz_k': player.find('blitz_k').text if player.find('blitz_k') is not None else None,
                'birthday': player.find('birthday').text if player.find('birthday') is not None else None,
                'flag': player.find('flag').text if player.find('flag') is not None else None,
            }
            data.append(player_data)
        except Exception as e:
            print(f"Error processing player: {e}")

    # Check if there is data in the list
    if not data:
        print("No player data found")
    else:
        print(f"Processed {len(data)} players")

    # Add an intermediate data check
    aux_df = pd.DataFrame(data)
    aux_df['file_name'] = file_name
    aux_df['data_coleta'] = datetime.now()
    df = pd.concat([df, aux_df])

try:
    print(df.head())
    # Save the DataFrame to a parquet file
    output_parquet_path = r'C:\Users\internal_path....parquet.gzip'
    df.to_parquet(output_parquet_path, index=False, compression='gzip')
    print(f"Data saved to {output_parquet_path}")
except Exception as e:
    print(f"Error creating DataFrame or saving to parquet: {e}")

