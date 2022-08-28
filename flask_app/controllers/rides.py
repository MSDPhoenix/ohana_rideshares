from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.ride import Ride
from flask_app.models.message import Message

def user():
    user_data = {
        "user_id" : session["user_id"]
    }
    return User.get_by_id(user_data)

@app.route("/rides_new/")
def rides_new():
    if "user_id" not in session:
        return redirect("/")
    return render_template("rides_new.html",user=user())

@app.route("/rides_one/<int:ride_id>/")
def rides_one(ride_id):
    if "user_id" not in session:
        return redirect("/")
    return render_template("rides_one.html",user=user())

@app.route("/rides_edit/<int:ride_id>/")
def ride_edit(ride_id):
    if "user_id" not in session:
        return redirect("/")
    return render_template("rides_edit.html",user=user())

@app.route("/rides_add/",methods=["POST"])
def rides_add():
    if "user_id" not in session:
        return redirect("/")
    if not Ride.validate(request.form):
        session["destination"] = request.form["destination"]
        session["pick_up_location"] = request.form["pick_up_location"]
        session["date"] = request.form["date"]
        session["details"] = request.form["details"]
        return redirect("rides_new.html")
    if "name" in session:
        session.pop("name")
    if "pick_up_location" in session:
        session.pop("pick_up_location")
    if "date" in session:
        session.pop("date")
    if "details" in session:
        session.pop("details")
    data = {
        "destination" : request.form["destination"],
        "pick_up_location" : request.form["pick_up_location"],
        "details" : request.form["details"],
        "date" : request.form["date"],
        "rider_id" : session["user_id"],
    }
    Ride.save(data)
    return redirect("/dashboard/")