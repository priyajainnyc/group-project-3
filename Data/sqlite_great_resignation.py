# sqlite_demo.py

import sqlite3
import pandas as pd

# use pandas to create dataframe based on csv data
df_linechartdata = pd.read_csv(r'D:\Data Science\16-Project-3-Data-Ethics\Group-Project-3\Data\line_chart_data.csv')
df_databystatemarch2023 = pd.read_csv(r'D:\Data Science\16-Project-3-Data-Ethics\Group-Project-3\Data\data_by_state_march_2023.csv')
df_top5industryannualquitrates = pd.read_csv(r'D:\Data Science\16-Project-3-Data-Ethics\Group-Project-3\Data\annual_quit_rates_top5.csv')
df_highestquitratesbystate = pd.read_csv(r'D:\Data Science\16-Project-3-Data-Ethics\Group-Project-3\Data\highest_quit_rates_by_state.csv')
df_sectorquits = pd.read_csv(r'D:\Data Science\16-Project-3-Data-Ethics\Group-Project-3\Data\sector_quits.csv')

# create a sqlite database and a connection to it
cnxn = sqlite3.connect('great_resignation.db')

# insert your dataframes into that database
df_linechartdata.to_sql('linechartdata', cnxn, index=False)
df_databystatemarch2023.to_sql('databystatemarch2023', cnxn, index=False)
df_top5industryannualquitrates.to_sql('top5industryannualquitrates', cnxn, index=False)
df_highestquitratesbystate.to_sql('highestquitratesbystate', cnxn, index=False)
df_sectorquits.to_sql('sectorquits', cnxn, index=False)

cnxn.close()

# success! you now have a sqlite database on your computer
