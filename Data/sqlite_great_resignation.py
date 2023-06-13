# sqlite_demo.py

import sqlite3
import pandas as pd

# use pandas to create dataframe based on csv data
df_linechartdata = pd.read_csv(r'line_chart_data.csv')
df_databystatemarch2023 = pd.read_csv(r'data_by_state_march_2023.csv')
df_top5industryannualquitrates = pd.read_csv(r'annual_quit_rates_top5.csv')

df_sectorquits = pd.read_csv(r'sector_quits.csv')

# create a sqlite database and a connection to it
cnxn = sqlite3.connect('great_resignation.db')
crsr = cnxn.cursor()

# create linechart table with a primary key
create_statement_linechart = """CREATE TABLE linechartdata (
Rates text PRIMARY KEY,
'column_2001' real,
'column_2002' real,
'column_2003' real,
'column_2004' real,
'column_2005' real,
'column_2006' real,
'column_2007' real,
'column_2008' real,
'column_2009' real,
'column_2010' real,
'column_2011' real,
'column_2012' real,
'column_2013' real,
'column_2014' real,
'column_2015' real,
'column_2016' real,
'column_2017' real,
'column_2018' real,
'column_2019' real,
'column_2020' real,
'column_2021' real,
'column_2022' real,
'column_2023' real
);"""
crsr.execute(create_statement_linechart)

# create databystatemarch table with a primary key
create_statement_databystatemarch2023 = """CREATE TABLE databystatemarch2023 (
State text PRIMARY KEY,
'HiresRate' real,
'HiresLevel' integer,
'JobOpeningsRate' real,
'JobOpeningsLevel' integer,
'QuitsRate' real,
'QuitsLevel' integer,
'Latitude' real,
'Longitude' real
);"""
crsr.execute(create_statement_databystatemarch2023)

# create top5industryannualquitrates table with a primary key
create_statement_top5industryannualquitrates = """CREATE TABLE top5industryannualquitrates (
Industry text PRIMARY KEY,
'column_2018' real,
'column_2019' real,
'column_2020' real,
'column_2021' real,
'column_2022' real
);"""
crsr.execute(create_statement_top5industryannualquitrates)



# create sectorquits table with a primary key
create_statement_sectorquits = """CREATE TABLE sectorquits (
Industry text PRIMARY KEY,
'column_2007' real,
'column_2008' real,
'column_2009' real,
'column_2010' real,
'column_2011' real,
'column_2012' real,
'column_2013' real,
'column_2014' real
);"""
crsr.execute(create_statement_sectorquits)



# insert your dataframes into that database
df_linechartdata.to_sql('linechartdata', cnxn, index=False, if_exists="append")
df_databystatemarch2023.to_sql('databystatemarch2023', cnxn, index=False, if_exists="append")
df_top5industryannualquitrates.to_sql('top5industryannualquitrates', cnxn, index=False, if_exists="append")

df_sectorquits.to_sql('sectorquits', cnxn, index=False, if_exists="append")

cnxn.close()

# success! you now have a sqlite database on your computer
