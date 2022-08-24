from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user
from flask_app.models import ride
db = "ohana_rideshares"

class Message:
    def __init__(self,data):
        self.id = data['id']
        self.sender_id = data['sender_id']
        self.ride_id = data['ride_id']
        self.content_id = data['content_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender = None

    def get_messages(cls,data):
        query = """
                SELECT * FROM messages 
                LEFT JOIN users
                ON messages.sender_id = users.id
                WHERE ride_id = %(ride_id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        messages = []
        for row in result:
            this_message = cls(row)
            sender_data = {
                "id" : row["xxx"],
                "first_name" : row["xxx"],
                "last_name" : row["xxx"],
                "email" : row["xxx"],
                "password" : row["xxx"],
                "created_at" : row["xxx"],
                "updated_at" : row["xxx"],
            }
            this_message.sender = user.User(sender_data)
            messages.append(this_message)
        return messages
             