# web_app/routes/home_routes.py

from flask import Blueprint, render_template

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

@home_routes.route("/user/create")
def regisetered():
    print("VISITED USER CREATED PAGE")
    #return "New user created page (TODO)"
    return render_template("created_user.html")

@home_routes.route("/new")
def new_quiz():
    print("VISITED NEW QUIZ PAGE")
    return "New quiz start page (TODO)"
    #return render_template("created_user.html")