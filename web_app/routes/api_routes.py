from flask import Blueprint, render_template, flash, request, redirect
from app.play_quiz import level_validation, load_database

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/get_quiz", methods=["POST"])
def api_get_quiz():
    quiz_details = dict(request.form)

    all_data = load_database()

    chosen_level = input("Choose a level: ")
    valid_level = level_validation(chosen_level)
    print("You chose Level ", valid_level, "\n")

    level_data = get_level_data(chosen_level)
    print(level_data)

    chosen_category = input("Choose a category: ")
    valid_category = category_validation(chosen_category)
    print("You chose the ", valid_category, "category", "\n")
    
    category_data = get_category_data(chosen_category)
    print(category_data)

