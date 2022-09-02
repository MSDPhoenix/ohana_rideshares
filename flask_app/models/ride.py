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
        self.driver = None
        # self.messages = []

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
    def get_all(cls):
        query = """
                SELECT * FROM rides
                LEFT JOIN users AS rider
                ON rider.id = rides.rider_id
                LEFT JOIN users AS driver
                ON driver.id = rides.driver_id
                ORDER BY date;
                """
        result = connectToMySQL(db).query_db(query)
        rides = []
        for row in result:
            this_ride = cls(row)
            rider_data = {
                "id" : row["rider.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["rider.created_at"],
                "updated_at" : row["rider.updated_at"],
            }
            this_ride.rider = user.User(rider_data)
            if row["driver.id"] != None:
                driver_data = {
                    "id" : row["driver.id"],
                    "first_name" : row["driver.first_name"],
                    "last_name" : row["driver.last_name"],
                    "email" : row["driver.email"],
                    "password" : row["driver.password"],
                    "created_at" : row["driver.created_at"],
                    "updated_at" : row["driver.updated_at"],
                }
                this_ride.driver = user.User(driver_data)
            rides.append(this_ride)
        return rides

    @classmethod
    def delete(cls,data):
        query = """
                DELETE FROM rides
                WHERE id = %(ride_id)s;
                """
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_driver(cls,data):
        query = """
                UPDATE rides 
                SET driver_id = %(driver_id)s
                WHERE id = %(ride_id)s;
                """
        connectToMySQL(db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = """
                UPDATE rides
                SET 
                pick_up_location=%(pick_up_location)s,
                details=%(details)s
                WHERE
                id = %(ride_id)s
                """
        connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = """
                SELECT * FROM rides 
                LEFT JOIN users AS driver
                ON rides.driver_id = driver.id
                LEFT JOIN users AS rider
                ON rides.rider_id = rider.id
                WHERE rides.id = %(ride_id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        ride = cls(result[0])
        rider_data = {
            "id" : result[0]["rider.id"],
            "first_name" : result[0]["rider.first_name"],
            "last_name" : result[0]["rider.last_name"],
            "email" : result[0]["rider.email"],
            "password" : result[0]["rider.password"],
            "created_at" : result[0]["rider.created_at"],
            "updated_at" : result[0]["rider.updated_at"],
        }
        driver_data = {
            "id" : result[0]["driver.id"],
            "first_name" : result[0]["first_name"],
            "last_name" : result[0]["last_name"],
            "email" : result[0]["email"],
            "password" : result[0]["password"],
            "created_at" : result[0]["driver.created_at"],
            "updated_at" : result[0]["driver.updated_at"],
        }
        ride.rider = user.User(rider_data)
        ride.driver = user.User(driver_data)
        return ride






    @staticmethod
    def validate(data):
        is_valid = True



        return is_valid



