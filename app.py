import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import (
    generate_password_hash, check_password_hash)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_dictionary")
def get_dictionary():
    dictionary = mongo.db.cockney_dictionary.find()
    return render_template("dictionary.html", dictionary=dictionary)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Check if user exists in db, create new dictionary
    if not for new user and store in db. Then make new user
    the current session cookie.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, that username is already taken")
            return redirect(url_for("register"))

        # otherwise store the information from form into below dictionary
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
            }
        # insert the dictionary variable into the db
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Thank you for registering to Pop Goes The Weasel")
        return redirect(url_for("register", username=session["user"]))

    return render_template("register.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        """Check if username exists in db."""
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
              existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for
                                ("user_profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


@app.route("/user_profile/<username>", methods=["GET", "POST"])
def user_profile(username):
    """Grab the session user's username from the db."""
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    dictionary = mongo.db.cockney_dictionary.find(
        {"added_by": session["user"]}
    )

    if session["user"]:
        return render_template(
            "user_profile.html", dictionary=dictionary, username=username)

    return redirect(url_for("sign_in"))


@app.route("/sign_out")
def sign_out():
    """Clear the session cookies to sign user out fully."""
    flash("You are now signed out!")
    session.clear()
    return redirect(url_for("sign_in"))


@app.route("/add_cockney", methods=["GET", "POST"])
def add_cockney():
    """
    Check user in session else redirect
    to home template.
    """
    if session["user"]:
        if request.method == "POST":
            word = {
                "word": request.form.get("word"),
                "meaning": request.form.get("meaning"),
                "added_by": session["user"]
            }

            mongo.db.cockney_dictionary.insert_one(word)

            flash("Thank you for contributing to Pop Goes The Weasel!")
            return redirect(url_for("add_cockney"))

        return render_template("add_cockney.html")
    else:
        return redirect(url_for("home"))


@app.route("/edit_cockney/<cockney_id>", methods=["GET", "POST"])
def edit_cockney(cockney_id):
    """
    Take new information from form and post to a new dictionary
    and add to db.
    """
    if request.method == "POST":
        submit = {
            "word": request.form.get("word"),
            "meaning": request.form.get("meaning"),
            "added_by": session["user"]
        }

        mongo.db.cockney_dictionary.update({"_id": ObjectId(cockney_id)}, submit)
        flash("Cockney Successfully Updated")

    cockney = mongo.db.cockney_dictionary.find_one(
          {"_id": ObjectId(cockney_id)})

    return render_template("edit_cockney.html", cockney=cockney)


@app.route("/delete_cockney/<cockney_id>")
def delete_cockney(cockney_id):
    """Remove record from database as selected by user"""
    mongo.db.cockney_dictionary.remove({"_id": ObjectId(cockney_id)})
    flash("Task Deleted")
    return redirect(url_for("add_cockney"))


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
