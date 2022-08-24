from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models import user
from flask_app.models import message
from flask_app.config.mysqlconnection import connectToMySQL
db = "ohana_rideshares"

class Message:
    def __init__(self,data):
        self.id = data["id"]
        self.content = data["id"]
        self.sender_id = data["id"]
        self.ride_id = data["id"]
        self.created_at = data["id"]
        self.updated_at = data["id"]
        self.sender = None

    @classmethod
    def get_messages_for_this_ride(cls,data):
        query = """
                SELECT * FROM messages WHERE ride_id = %(ride_id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        messages = []
        for row in result:
            this_message = cls(row)
            messages.append(this_message)
        return messages
    
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO messages
                (content,sender_id,ride_id)
                VALUES
                (%(content)s,%(sender_id)s,%(ride_id)s)
                """
        user_id = connectToMySQL(db).query_db(query,data)
        return user_id
    
    @classmethod
    def delete(cls,data):
        pass