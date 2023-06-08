import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///great_resignation.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Rates = Base.classes.rates

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
    return (
        f"Welcome to the Great Resignation API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/annual-quit-rates/Recession<br/>"
        f"/api/v1.0/annual-quit-rates/Covid-19"
    )

@app.route("/api/v1.0/annual-quit-rates/Covid-19")
def quit_rates_covid():
    results = session.query.all()
    session.close()
    return jsonify(results)

@app.route("/api/v1.0/Industry")
def Industry():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Rates.Industry).all()

    session.close()

    # Convert list of tuples into normal list
    all_industry = list(np.ravel(results))

    return jsonify(all_industry)

@app.route("/api/v1.0/quit-rates/Covid-19")
def quit_rates():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query().all()

    session.close()

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

    return jsonify(all_rates)

@app.route("/api/v1.0/Ratesbyindustry/<Industry>")
def rates_by_industry(Industry):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all 
    results = session.query().all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_rates = []
    for Industry in results:
        rates_dict = {}
        rates_dict["Industry"] = Industry
        rates_dict["2018"] = 2018
        rates_dict["2019"] = 2019
        rates_dict["2020"] = 2020
        rates_dict["2021"] = 2021
        rates_dict["2022"] = 2022
        all_rates.append(rates_dict)

    return jsonify(all_rates)

if __name__ == "__main__":
    app.run(debug=True)
