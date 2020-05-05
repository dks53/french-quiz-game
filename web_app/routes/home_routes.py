# web_app/routes/home_routes.py

from flask import Blueprint, render_template, flash, request, redirect
from app.play_quiz import get_category_data, get_level_data, load_database, send_email
from random import shuffle
import json
#from prettytable import PrettyTable

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
    flash(f"User '{user['user_name']}' created successfully!", "success")
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

    all_data = load_database()

    level_data = get_level_data(setup_info['lvl'], all_data)
    category_data = get_category_data(setup_info['categ'], level_data)

    shuffle(category_data)

    questions = []

    count = 1
    for question in category_data:
        if count <= int(setup_info['len']):
            payload = {
                "number": count,
                "english_word": question["english_word"],
                "french_word": question["french_word"]
            }

            questions.append(payload)
        else:
            break
        count = count + 1
    print("END OF NEW QUIZ")
    # questions must contain english word and ID
    return render_template("quiz_uncompleted.html", questions=questions, quiz_params=setup_info)
    #return render_template("quiz_setup.html")

@home_routes.route("/new/feedback", methods=["POST"])
def new_quiz_end():
    print("VISITED NEW QUIZ SCORE PAGE")
    #print("FORM DATA:", dict(request.form))
    quiz_info = dict(request.form)
    #print("QUIZ INFO: ", quiz_info)
    quiz_length = int(quiz_info['quiz_length'])
    feedbacks = []

    setup_info = {
        'lvl': quiz_info['quiz_level'],
        'categ': quiz_info['quiz_cat'],
        'len': quiz_info['quiz_length']
    }

    for i in range(1, quiz_length + 1):
        question = str(i)
        count = 0
        collected_responses = {
            "number": i,
            "correct": quiz_info[question].lower() == quiz_info[question + "_answer"].lower(),
            "user_response": quiz_info[question],
            "french_word": quiz_info[question + "_answer"]
        }

        feedbacks.append(collected_responses)

    score_count = 0
    for feedback in feedbacks:
        if feedback["correct"] == True:
            score_count = score_count + 1
        else:
            score_count
    
    #print(score_count)
    percent_score = round((float(score_count)/float(setup_info['len']))*100,2)
    #print(percent_score)

    comment = ""

    if percent_score == 100:
        comment = "That's a perfect score! Great job!"
    elif percent_score < 100 and percent_score >= 85:
        comment = "Great going! You're almost there!"
    elif percent_score < 85 and percent_score >= 60:
        comment = "Don't worry, you just need some more practice"
    elif percent_score < 60:
        comment = "What happened there? You need to work harder!"
    else:
        comment = "IF THIS SHOWS UP, SOMETHING'S WRONG"

    #print("Feedbacks: ", feedbacks)
    #print("Quiz Params: ", setup_info)
    #print("Score: ", score_count)
    #print("Percent: ", percent_score)
    #print("Comment: ", comment)

    feedbacks_string = json.dumps(feedbacks)

    return render_template("quiz_feedback.html", feedbacks=feedbacks, quiz_params=setup_info, 
    score_count=score_count, percent_score=percent_score, comment=comment, feedbacks_string=feedbacks_string)
    #return render_template("quiz_setup.html")

@home_routes.route("/new/quiz_completed", methods=["POST"])
def quiz_result_email():
    print("VISITED POST EMAIL QUIZ END PAGE")

    #email_report_to = dict(request.form)
    #print(email_report_to['email_address'])

    quiz_info = dict(request.form)
    quiz_info['feedbacks'] = json.loads(quiz_info['feedbacks'])
    email_report_to = quiz_info['email_address']
    #print("QUIZ INFO: ", quiz_info)
    #print("FEEDBACKS: ", quiz_info['feedbacks'])
    quiz_length = int(quiz_info['quiz_length'])
    #feedbacks = []

    setup_info = {
        'lvl': quiz_info['quiz_level'],
        'categ': quiz_info['quiz_cat'],
        'len': quiz_info['quiz_length']
    }

    send_email(to=email_report_to, html=generate_email_feedback(quiz_info))

    flash(f"Quiz score emailed to '{email_report_to}' successfully!", "success")

    return render_template("quiz_completed.html", quiz_info=quiz_info, email_report_to=email_report_to, feedbacks=quiz_info['feedbacks'])

def generate_email_feedback(quiz_info):
    header = f"""    
    <h3> Student Name: {quiz_info['name']} </h3>
    <br>
    Level: {quiz_info['quiz_level']} <br>
    Categroy: {quiz_info['quiz_cat']} <br>
    Quiz Length: {quiz_info['quiz_length']} <br>
    """

    content = f"""
    <br>
    <br>
    <table style="width: 50%;">
        <thead>
            <td><b>#</b></td>
            <td><b>Your Answer</b></td> 
            <td><b>Correct Answer</b></td> 
            <td><b>Correct?</b></td></thead>
        </thead>
    """
    for feedback in quiz_info['feedbacks']:
        content += f"""
        <tr>
            <td> {feedback['number']}. </td>
            <td> {feedback['user_response']} </td>
            <td> {feedback['french_word']} </td>
            <td>
            """
        if feedback["correct"]:
            content += "<label style = 'color:green;'> ✅ Correct</label>"
        else:
            content += "<label style = 'color:red;'> ❌ Incorrect</label>"
        content += "</td>"
        content += "</tr>"
    
    content += "</table>"

    #print(content)

    footer = f"""

    <br>
    ************************** <br>
    <b> Final Score: {quiz_info['score_count']} out of {quiz_info['quiz_length']} </b> <br>
    <b> Comment: {quiz_info['comment']} </b>

    """

    return header + "\n" + content + "\n" + footer

@home_routes.route("/project_feedback")
def collect_feedback():
    print("VISITED GET USER FEEDBACK PAGE")
    return render_template("collect_feedback.html")

@home_routes.route("/submitted_feedback", methods=["POST"])
def received_feedback():
    print("VISITED FEEDBACK SUBMITTED CONFIRMATION PAGE")
    feedback_info = dict(request.form)
    print(feedback_info)

    send_email(html=send_feedback(feedback_info), subject="French Quiz App Feedback")

    flash(f"Feedback emailed successfully!", "success")

    return render_template("submitted_feedback.html", feedback_info=feedback_info)

def send_feedback(feedback_info):
    email_content = f"""    
    Name: {feedback_info['name']} <br>
    <br>
    Email ID: {feedback_info['email_address']} <br>
    <br>
    Comment: {feedback_info['comment']} <br>
    """
    return email_content