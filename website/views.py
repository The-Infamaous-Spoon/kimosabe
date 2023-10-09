from flask import Blueprint, render_template, flash, request, session, url_for, redirect
from .models import Users
from . import db

views = Blueprint('views',__name__)

@views.route("/", methods=["POST", "GET"])
def return_home():
    if request.method == "POST":
        email = request.form.get("email_input")
        #session["email"] = email
        user = Users.query.filter_by(user_email=email).first()
        if len(email) > 0:
            flash('PENIS', category='success')
            return render_template('index.html')
        else:
            return render_template('index.html')

            # print('penis')
            # flash('PENIS',category='success')
            # return render_template("index.html")
    else:
        #flash('try again', category='error')
        return  render_template('index.html')

@views.route("/email")
def user():
    if "email" in session:
        # email = session["email"]
        return render_template("thanks.html")
    else:
        return redirect(url_for("views.return_home"))
