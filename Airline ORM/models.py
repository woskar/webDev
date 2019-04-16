import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    # note: the following passengers colum is not part of the table "flights"
    # it's defined as relationship to connect tables "flights" and "passengers" together
    # with passengers we can extract the Passengers directly from the flights table
    # the backref works in the other way, let's us get the flights of a passenger
    # lazy=True won't fetch all the data unless needed for efficiency reasons
    passengers = db.relationship("Passenger", backref="flight", lazy=True)
    # Using dot-notation we can extract all passengers on a flight

    def add_passenger(self, name):
        p = Passenger(name=name, flight_id=self.id)
        db.session.add(p)
        db.session.commit()


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
