from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Tri_Sparkers")

@views.route("/profile")
def profile():
    return render_template("profile.html")


@views.route("/json")
def get_json():
    return jsonify({'hi': 'Welcome to our catering service', 'hi': 'We will provide every dishes'})



@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/got-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

