# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.get("measurement")
Station = Base.classes.get("station")

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################


# Initialize Flask app
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Homepage route that lists available routes
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    # Find the most recent date in the dataset
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    
    # Calculate the date one year from the last date in dataset
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

    # Query last 12 months of precipitation data
    results = session.query(Measurement.date, Measurement.prcp)\
        .filter(func.strftime("%Y-%m-%d", Measurement.date) >= one_year_ago.strftime("%Y-%m-%d"))\
        .filter(Measurement.prcp.isnot(None))\
        .order_by(Measurement.date).all()

    session.close()

    # Convert query results into dictionary format
    precipitation_dict = {date: prcp for date, prcp in results}
    
    return jsonify(precipitation_dict)

# Stations Route
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    # Query all stations
    results = session.query(
        Station.station, func.count(Measurement.tobs)
    ).join(Measurement, Station.station == Measurement.station)\
    .group_by(Station.station)\
    .order_by(func.count(Measurement.tobs).desc()).all()
    
    session.close()

    # Convert list of tuples into normal list
    station_list = [{"station": station, "observation_count": count} for station, count in results]
    
    return jsonify(station_list)

# Temperature Observations (TOBS) Route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    # Find the most active station
    active_stations = session.query(
        Measurement.station, func.count(Measurement.station)
    ).group_by(Measurement.station)\
    .order_by(func.count(Measurement.station).desc()).all()

    most_active_station = active_stations[0][0]

    # Find the most recent date
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

    # Query last 12 months of temperature observations for the most active station
    results = session.query(Measurement.tobs)\
        .filter(Measurement.station == most_active_station)\
        .filter(Measurement.date >= one_year_ago).all()

    session.close()

    # Convert list of tuples into normal list
    temperature_observations = [{"date": date, "temperature": tobs} for date, tobs in results]
    
    return jsonify(temperature_observations)

# Dynamic route for temperature stats based on start date
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_range(start, end=None):
    session = Session(engine)

    # Query for min, avg, and max temperatures
    query = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start)

    # If an end date is provided, apply it to the filter
    if end:
        query = query.filter(Measurement.date <= end)

    result = query.all()
    
    session.close()

    # Convert results into a dictionary including start_date and end_date
    temperature_dict = {
        "start_date": start,
        "TMIN": result[0][0],
        "TAVG": round(result[0][1], 2),  # Rounded for better readability
        "TMAX": result[0][2]
    }

    # Add the end date only if it exists
    if end:
        temperature_dict["end_date"] = end
    
    return jsonify(temperature_dict)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)