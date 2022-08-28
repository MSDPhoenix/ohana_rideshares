from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models import user
from flask_app.models import message
from flask_app.config.mysqlconnection import connectToMySQL
db = "ohana_rideshares"

class Ride:
    def __init__(self,data):
        self.id = data["id"]
        self.destination = data["destination"]
        self.pick_up_location = data["pick_up_location"]
        self.details = data["details"]
        self.date = data["date"]
        self.rider_id = data["rider_id"]
        self.driver_id = data["driver_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.rider = None
        self.driver_id = None
        self.messages = []

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO rides
                (destination,pick_up_location,details,rider_id,date)
                VALUES 
                (%(destination)s,%(pick_up_location)s,%(details)s,%(rider_id)s,%(date)s);
                """
        ride_id = connectToMySQL(db).query_db(query,data)
        return ride_id

    @classmethod
    def xxx(cls,data):
        pass

    @staticmethod
    def validate(data):
        is_valid = True
        return is_valid



