import sqlite3
import pandas as pd

df_barchart = pd.read_csv("Data.clean/08-18sectordata22.csv")

cnxn = sqlite3.connect("sector_data.db")

df_barchart.to_sql("sector_data", cnxn, index=False)

cnxn.close()

                       
