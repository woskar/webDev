from flask import Flask, render_template, jsonify, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    """
    Index route gives dropdown menu to register for flight.
    So first query all of the flights in the database. 
    Then turn the existing flights and the html to be rendered.
    """
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    """
    Book a flight.
    Users provide their information and select flight. 
    """

    # Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists.
    flight = Flight.query.get(flight_id)
    if not flight: # similar to "if flight is None:"
        return render_template("error.html", message="No such flight with that id.")

    '''
    # Add passenger - Version 1: passenger added explicitely to table
    passenger = Passenger(name=name, flight_id=flight_id)
    db.session.add(passenger) # insert passenger in the passengers table
    db.session.commit() # commit / execute the changes
    return render_template("success.html")
    '''

    # Add passenger - Version 2: function add_passenger achieves functionality of Version 1 
    flight.add_passenger(name)
    return render_template("success.html")
    

@app.route("/flights")
def flights():
    """List all flights."""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")

    """
    # Get all passengers - Version 1: extract via usual SQLAlchemy-syntax
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    """

    # Get all passengers - Version 2: achieved by relationship in models.py
    # flight gets the relationship passengers, so we can now access the passengers-table
    # as if it was part of the flight table itself.
    # Using dot-notation we can extract all passengers on a flight
    passengers = flight.passengers
    return render_template("flight.html", flight=flight, passengers=passengers)


@app.route("/api/flights/<int:flight_id>")
# Implements API-interface for others to use
def flight_api(flight_id):
    """Return details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        # return correctly formatted error response with an error code
        return jsonify({"error": "Invalid flight_id"}), 422

    # Get all passengers
    passengers = flight.passengers
    names = [] # store names
    for passenger in passengers:
        names.append(passenger.name)
    # return the machine-readable JSON-Object
    return jsonify({
            "origin": flight.origin,
            "destination": flight.destination,
            "duration": flight.duration,
            "passengers": names
        })
