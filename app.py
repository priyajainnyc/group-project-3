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

if __name__ == "__main__":
    app.run(debug=True)
