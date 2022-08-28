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
                ON driver.id = rides.driver_id;
                """
        result = connectToMySQL(db).query_db(query)
        print("A")
        rides = []
        for row in result:
            for item in row:
                print(item,"\t\t",row[item])
                # print("      = ",row[item])
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
    def delete(data):
        query = """
                
                """







    @staticmethod
    def validate(data):
        is_valid = True



        return is_valid



