from flask import Blueprint, render_template, flash, request

views = Blueprint('views',__name__)

@views.route("/", methods=["GET", "POST"])
def return_home():
    return render_template("index.html")
