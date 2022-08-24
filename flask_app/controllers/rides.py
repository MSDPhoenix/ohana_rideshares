from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.ride import Ride
from flask_app.models.message import Message

def logged_in_user():
    user_data = {
        "user_id" : session["user_id"]
    }
    return User.get_by_id(user_data)

@app.route("/dashboard/")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    return render_template("dashboard.html",user=logged_in_user())

@app.route("/rides_new/",methods=["POST"])
def rides_new():
    if "user_id" not in session:
        return redirect("/")
    return render_template("rides_new.html",user=logged_in_user())

@app.route("/rides_one/<int:ride_id>/")
def rides_one(ride_id):
    if "user_id" not in session:
        return redirect("/")
    return render_template("rides_one.html",user=logged_in_user())

@app.route("/rides_edit/<int:ride_id>/",methods=["POST"])
def ride_edit(ride_id):
    if "user_id" not in session:
        return redirect("/")
    return render_template("rides_edit.html",user=logged_in_user())