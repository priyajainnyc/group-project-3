import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

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
highestquitratesbystate = Base.classes.highestquitratesbystate
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
    Currently, the only api route accessed by the web page is 'passengersbyclass'.
    """
    return render_template('index.html')

@app.route("/api/v1.0/annual-quit-rates/Covid-19")
def quit_rates_covid():
    results = session.query.all()
    session.close()
    return jsonify(results)

# @app.route("/api/v1.0/Industry")
# def Industry():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(top5industryannualquitrates).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_industry = list(np.ravel(results))

#     return jsonify(all_industry)

# @app.route("/api/v1.0/quit-rates/Covid-19")
# def quit_rates():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query().all()

#     session.close()

    # Create a dictionary from the row data and append to a list of all_rates
    all_rates = []
    for Industry in results:
        rates_dict = {}
        # rates_dict["Industry"] = Industry
        # rates_dict["2018"] = 2018
        # rates_dict["2019"] = 2019
        # rates_dict["2020"] = 2020
        # rates_dict["2021"] = 2021
        # rates_dict["2022"] = 2022
        all_rates.append(rates_dict)

#     return jsonify(all_rates)

# @app.route("/api/v1.0/Ratesbyindustry/<Industry>")
# def rates_by_industry(Industry):
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all 
#     results = session.query().all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_rates = []
#     for Industry in results:
#         rates_dict = {}
#         rates_dict["Industry"] = Industry
#         rates_dict["2018"] = 2018
#         rates_dict["2019"] = 2019
#         rates_dict["2020"] = 2020
#         rates_dict["2021"] = 2021
#         rates_dict["2022"] = 2022
#         all_rates.append(rates_dict)

#     return jsonify(all_rates)

if __name__ == "__main__":
    app.run(debug=True)
