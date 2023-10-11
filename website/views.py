from flask import Blueprint, render_template, flash, request, session, url_for, redirect, jsonify
from .models import Users
from . import db

views = Blueprint('views', __name__)

@views.route("/", methods=["POST", "GET"])
def return_home():
    session.clear()
    if request.method == "POST":
        email = request.form.get("email_input")
        user = Users.query.filter_by(user_email=email).first()

        if len(email) > 0:
            user = Users.query.filter_by(user_email=email).first()

            if user:
                # Store the email and user_tokens in the session
                session["email"] = email
                session["user_tokens"] = user.user_tokens
                return redirect(url_for("views.user"))
            else:
                user = Users(user_email=email, user_tokens=float(1.000000))
                db.session.add(user)
                db.session.commit()
                flash('User added', category="success")
                # Store the email and user_tokens in the session
                session["email"] = email
                session["user_tokens"] = user.user_tokens
                return redirect(url_for("views.user"))
            return render_template('index.html')
        else:
            return render_template('index.html')
    else:
        # Clear the session
        session.clear()
        return render_template('index.html')

@views.route("/user", methods=["POST", "GET"])
def user():
    email = session.get("email")
    user = Users.query.filter_by(user_email=email).first()

    if email and user:
        user_tokens = user.user_tokens

        if request.method == 'GET':
            return render_template("thanks.html", user_tokens=user_tokens, email=email)
        elif request.method == "POST":
            data = request.get_json()
            new_tokens = data.get("user_tokens")

            # Update the user's tokens in the database (assuming you have the user object)
            if user:
                user.user_tokens = new_tokens
                db.session.commit()
                return jsonify({'message': 'Tokens updated successfully'})
            else:
                return jsonify({'error': 'User not found'})

    return redirect(url_for("views.return_home"))
