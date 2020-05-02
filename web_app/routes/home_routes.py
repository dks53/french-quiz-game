# web_app/routes/home_routes.py

from flask import Blueprint, render_template, flash, request, redirect

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    #return "Welcome Home (TODO)"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    #return "About Me (TODO)"
    return render_template("about.html")

@home_routes.route("/instructions")
def rules():
    print("VISITED THE INSTRUCTIONS PAGE")
    #return "How to play the game (TODO)"
    return render_template("instructions.html")

@home_routes.route("/user/new")
def register():
    print("VISITED THE REGISTRATION PAGE")
    #return "New user page (TODO)"
    return render_template("signup.html")

@home_routes.route("/user/create", methods=["POST"])
def regisetered():
    print("VISITED USER CREATED PAGE")
    user = dict(request.form)
    #print("FORM DATA:", dict(request.form))
    print("FORM DATA:", user)
    # todo: store in a database or google sheet!
    flash(f"User '{user['first_name']}' created successfully!", "success")
    #return "New user created page (TODO)"
    return redirect("/")

@home_routes.route("/new/setup")
def new_quiz_setup():
    print("VISITED NEW QUIZ SETTINGS PAGE")
    #return "New quiz settings page (TODO)"
    return render_template("quiz_setup.html")

@home_routes.route("/new/start", methods=["POST"])
def new_quiz_start():
    print("VISITED NEW QUIZ START PAGE")
    #print("FORM DATA:", dict(request.form))
    setup_info = dict(request.form)
    print(setup_info)
    return "New quiz start page (TODO)"
    #return render_template("quiz_setup.html")