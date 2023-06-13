import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import pandas as pd

from flask import Flask, jsonify, render_template

#################################################
# Database Setup
#################################################
engine = create_engine(r"sqlite:///Data\great_resignation.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
linechartdata = Base.classes.linechartdata
databystatemarch2023 = Base.classes.databystatemarch2023
top5industryannualquitrates = Base.classes.top5industryannualquitrates
sectorquits = Base.classes.sectorquits

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """
    Render the main page of the webapp.

    """
    return render_template('index.html')

@app.route("/api/v1.0/ratesdata")
def ratesdata():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(linechartdata.Rates, linechartdata.column_2001, linechartdata.column_2002, linechartdata.column_2003, linechartdata.column_2004, linechartdata.column_2005, linechartdata.column_2006, linechartdata.column_2007, linechartdata.column_2008, linechartdata.column_2009, linechartdata.column_2010, 
                            linechartdata.column_2011, linechartdata.column_2012, linechartdata.column_2013, linechartdata.column_2014, linechartdata.column_2015, linechartdata.column_2016, linechartdata.column_2017, linechartdata.column_2018, linechartdata.column_2019, linechartdata.column_2020, 
                            linechartdata.column_2021, linechartdata.column_2022, linechartdata.column_2023).all()
    session.close()

    df = pd.DataFrame(results)
    rate_names = list(df["Rates"])
    categories_and_values = {}
    for rname in rate_names:
        rates_series = df.loc[df["Rates"]==rname].iloc[:,1:]
        rates_values = list(rates_series.values[0])
        rates_years = list(range(2001,2024))
        categories_and_values[rname] = {"Rates":rates_values, "Years": rates_years}
    print(categories_and_values)
    rateslist = []
    for Rates, column_2001, column_2002, column_2003, column_2004, column_2005, column_2006, column_2007, column_2008, column_2009, column_2010, column_2011, column_2012, column_2013, column_2014, column_2015, column_2016, column_2017, column_2018, column_2019, column_2020, column_2021, column_2022, column_2023 in results:
        all_rates = {}
        all_rates["Rates"] = Rates
        all_rates["2001"] = column_2001
        all_rates["2002"] = column_2002
        all_rates["2003"] = column_2003
        all_rates["2004"] = column_2004
        all_rates["2005"] = column_2005
        all_rates["2006"] = column_2006
        all_rates["2007"] = column_2007
        all_rates["2008"] = column_2008
        all_rates["2009"] = column_2009
        all_rates["2010"] = column_2010
        all_rates["2011"] = column_2011
        all_rates["2012"] = column_2012
        all_rates["2013"] = column_2013
        all_rates["2014"] = column_2014
        all_rates["2015"] = column_2015
        all_rates["2016"] = column_2016
        all_rates["2017"] = column_2017
        all_rates["2018"] = column_2018
        all_rates["2019"] = column_2019
        all_rates["2020"] = column_2020
        all_rates["2021"] = column_2021
        all_rates["2022"] = column_2022
        all_rates["2023"] = column_2023
        rateslist.append(all_rates)
        
    return categories_and_values

@app.route("/api/v1.0/quitrates_covid19_byindustry")
def quitrates_covid19_byindustry():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of quitrates in 2018-2022 by industry"""
    # Query all
    results = session.query(top5industryannualquitrates.Industry, top5industryannualquitrates.column_2018, top5industryannualquitrates.column_2019, top5industryannualquitrates.column_2020, top5industryannualquitrates.column_2021, top5industryannualquitrates.column_2022).all()
    session.close()
    # Create a dictionary from the row data and append to a list of all_rates
    df = pd.DataFrame(results)
    industry_names = list(df["Industry"])
    categories_and_values = {}
    for rname in industry_names:
        rates_series = df.loc[df["Industry"]==rname].iloc[:,1:]
        rates_values = list(rates_series.values[0])
        rates_years = list(range(2018,2023))
        categories_and_values[rname] = {"Rates":rates_values, "Years": rates_years}
    print(categories_and_values)
    # Create a dictionary from the row data and append to a list of all_rates
    all_quitrates = []
    for Industry, column_2018, column_2019, column_2020, column_2021, column_2022 in results:
        quitrates_covid19_dict = {}
        quitrates_covid19_dict["Industry"] = Industry
        quitrates_covid19_dict["2018"] = column_2018
        quitrates_covid19_dict["2019"] = column_2019
        quitrates_covid19_dict["2020"] = column_2020
        quitrates_covid19_dict["2021"] = column_2021
        quitrates_covid19_dict["2022"] = column_2022
        all_quitrates.append(quitrates_covid19_dict)
   
    return categories_and_values

@app.route("/api/v1.0/sectorquits")
def sectorrates():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query all
    results1 = session.query(sectorquits.Industry, sectorquits.column_2007, sectorquits.column_2008,
                            sectorquits.column_2009, sectorquits.column_2010,
                            sectorquits.column_2011,sectorquits.column_2012,
                            sectorquits.column_2013,sectorquits.column_2014,
                            ).all()
    session.close()
    # Create a dictionary from the row data and append to a list of all_rates
    df = pd.DataFrame(results1)
    industry_names = list(df["Industry"])
    categories_and_values = {}
    for rname in industry_names:
        rates_series = df.loc[df["Industry"]==rname].iloc[:,1:]
        rates_values = list(rates_series.values[0])
        rates_years = list(range(2007,2015))
        categories_and_values[rname] = {"Rates":rates_values, "Years": rates_years}
    print(categories_and_values)
    # Create a dictionary from the row data and append to a list of all_rates
    all_sectors = []
    for Industry, column_2007, column_2008, column_2009, column_2010, column_2011, column_2012, column_2013, column_2014 in results1:
        quitrates_recession_dict1 = {}
        quitrates_recession_dict1["Industry"] = Industry
        quitrates_recession_dict1["2007"] = column_2007
        quitrates_recession_dict1["2008"] = column_2008
        quitrates_recession_dict1["2009"] = column_2009
        quitrates_recession_dict1["2010"] = column_2010
        quitrates_recession_dict1["2011"] = column_2011
        quitrates_recession_dict1["2012"] = column_2012
        quitrates_recession_dict1["2013"] = column_2013
        quitrates_recession_dict1["2014"] = column_2014
        all_sectors.append(quitrates_recession_dict1)
    
    return categories_and_values

if __name__ == "__main__":
    app.run(debug=True)
