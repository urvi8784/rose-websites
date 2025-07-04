from flask import Blueprint, render_template

roses = Blueprint("roses", __name__)

@roses.route("/")
def home():
    return render_template("index.html")

@roses.route("/rose1")
def rose1():
    return render_template("rose1.html")

@roses.route("/mythical-roses")
def mythical_roses():
    return render_template("mythical-roses.html")

@roses.route("/symbolism")
def symbolism():
    return render_template("symbolism.html")
