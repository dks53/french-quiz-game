# app/play_quiz.py

## IMPORTING PYTHON PACKAGES AND MODULES 
import csv
import random
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")

## FUNCTION DEFINITIONS (w/DOCSTRING COMMENTS)
def load_database():
    """
    Loads the vocabulary database stored in the "data" folder of the repository.

    Params:
        No params to call this function. All code is executed within the function.

    Examples:
        load_database()
    """
    #csv_file_path = "words_database.csv" # a relative filepath
    csv_file_path = os.path.join(os.path.dirname(__file__), "../data", "words_database.csv")
    all_data = [] # list containing all data from the database

    with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
        reader = csv.DictReader(csv_file) # assuming your CSV has headers
        # reader = csv.reader(csv_file) # if your CSV doesn't have headers
        for row in reader:
            #print(row["gender"], row["french_word"], row["english_word"], row["category"], row["level"])
            all_data.append(dict(row))

    return all_data

def level_validation(user_level, all_data_info):
    """
    Check if the level selected by the user exists in the database.
    Returns the level number entered by the user, if it exists. 
    If the level entered doesn't exist, it returns an error message and exits the program.

    Params:
        1) user_level - This is the input received from the user
        2) all_data_info - This is the list containing all the information from the database

    Examples:
        valid_level = level_validation(chosen_level, all_data)
        > valid_level = level_validation("1", all_data)
        > valid_level = "1"

        valid_level = level_validation(chosen_level, all_data)
        > valid_level = level_validation("100192", all_data)
        > "You chose an invalid level, please try again", exit()
    """
    count = 0
    for data in all_data_info:
        if data["level"] == user_level:
            count = count + 1
        else:
            pass
    
    if count == 0:
        return print("You chose an invalid level, please try again"), exit()
    else:
        return user_level

def get_level_data(user_level, all_data_info):
    """
    Loops through the all_data list and adds the rows that match with the user selected level 
    to a new list called level_data.

    Params:
        1) user_level - This is the input received from the user
        2) all_data_info - This is the list containing all the information from the database

    Examples:
        level_data = get_level_data(chosen_level, all_data)
        > level_data = get_level_data("1", all_data)
        > level_data = [...] list containing rows of information that correspond to level 1.
    """
    level_data = []

    for data in all_data_info:
        if data["level"] == user_level:
            level_data.append(data)
        else:
            pass
    
    return level_data

def category_validation(user_category, level_data_info):
    """
    Check if the category selected by the user exists in the level_data list.
    Returns the level number entered by the user, if it exists. 
    If the level entered doesn't exist, it returns an error message and exits the program.

    Params:
        1) user_category - This is the input received from the user
        2) level_data_info - This is the list containing the contents level_data.

    Examples:
        valid_category = category_validation(chosen_category, level_data)
        > valid_category = category_validation("animals", level_data)
        > valid_category = "animals"

        valid_category = category_validation(chosen_category, level_data)
        > valid_category = category_validation("animals", level_data)
        > "You chose an invalid category, please try again", exit()
    """

    count = 0
    for data in level_data_info:
        if data["category"] == user_category:
            count = count + 1
        else:
            pass
    
    if count == 0:
        return print("You chose an invalid category, please try again"), exit()
    else:
        return user_category

def get_category_data(user_category, level_data_info):
    """
    Loops through the level_data list and adds the rows that match with the user selected category 
    to a new list called category_data.

    Params:
        1) user_category - This is the input received from the user.
        2) level_data_info - This is the list containing the contents level_data.

    Examples:
        category_data = get_category_data(chosen_category, level_data)
        > category_data = get_category_data("animals", level_data)
        > category_data = [...] list containing rows of information that correspond to the "animals" category.
    """
    category_data = []
    for data in level_data_info:
        if data["category"] == user_category:
            category_data.append(data)
        else:
            pass
        
    return category_data

def get_eng_word(category_data):
    """
    Takes the category_data list and appends the values corresponding to the 
    "english_word" key, to a new list called eng_words.

    Params:
        1) category_data - list containing all the information that corresponds to the user's selected level and category

    Examples:
        eng_words = get_eng_word(category_data)
        > eng_words = ['dog','cat'...]
    """    
    
    eng_words = []
    for data in category_data:
        eng_word = data["english_word"]
        eng_words.append(eng_word)
    
    return eng_words

def get_fren_word(category_data):
    """
    Takes the category_data list and appends the values corresponding to the 
    "french_word" key, to a new list called fren_words.

    Params:
        1) category_data - list containing all the information that corresponds to the user's selected level and category

    Examples:
        fren_words = get_fren_word(category_data)
        > fren_words = ['chien','chat'...]
    """    

    fren_words = []
    for data in category_data:
        fren_word = data["french_word"]
        fren_words.append(fren_word)
    
    return fren_words

def get_quiz(quiz_length):
    """
    This is the function that actually runs the quiz by displaying an english word from the eng_words list
    and asking the user for a french translation. It takes the user's reponse and compares it to the coorect answer
    that is in the fren_words list. If the answer matches, the score counter increases by 1, else it remains as it is.

    Params:
        1) quiz_length - This is the number of questions in the quiz, selected by the user. This number ensures that
        the questions don't loop infinitely.

    Examples:
        final_score = get_quiz(5)
        > final_score = 3
    """    
    n = 0
    final_score = 0

    while n < quiz_length:
        answer = input("What is the french word for " + eng_words[shuffled_list[n]] + "? ")
        if answer == fren_words[shuffled_list[n]]:
            print("CORRECT!")
            print("")
            final_score = final_score + 1
            n = n + 1
        else:
            print("INCORRECT")
            print("The correct answer is " + fren_words[shuffled_list[n]])
            print("")
            n = n + 1
    
    return final_score

def send_email(subject="French Quiz Score Report", html="", to=MY_EMAIL):
    """
    This function takes the final outputs such as the results of the quiz and specific quiz details and sends 
    an email report via SendGrid. 

    Params:
        1) subject - determines the subject of the email (pre-decided)
        2) html - this is the main content of the email that is taken from the 
           generate_email_feedback function in routes/home_routes.py
        3) to - this is the email address to which the email needs to be sent.
           The default value is set as the email address associated with the send grid account
           and can be found in the .env file

    Examples:
        send_email(subject, content, email_address)
        > send_email(subject="French Quiz Score Report", html="", to=MY_EMAIL)
        > 202 indicating success.

    """    
    
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    #print("CLIENT:", type(client))
    #print("SUBJECT:", subject)
    #print("HTML:", html)
    message = Mail(from_email=MY_EMAIL, to_emails=to, subject=subject, html_content=html)
    try:
        response = client.send(message)
        #print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", e.message)
        return None

## USER INPUTS AND SYSTEM OUTPUTS
if __name__ == "__main__":

    all_data = load_database()
    #print(all_data)

    chosen_level = input("Choose a level: ")
    valid_level = level_validation(chosen_level, all_data)
    print("You chose Level ", valid_level, "\n")

    level_data = get_level_data(chosen_level, all_data)
    #print(level_data)

    chosen_category = input("Choose a category: ")
    valid_category = category_validation(chosen_category, level_data)
    print("You chose the ", valid_category, "category", "\n")
    
    category_data = get_category_data(chosen_category, level_data)
    #print(category_data)

    quiz_length = input("How many questions would you like in the quiz? ")
    quiz_length = int(quiz_length)
    #print(quiz_length)

    eng_words = get_eng_word(category_data)
    #print(eng_words)

    fren_words = get_fren_word(category_data)
    #print(fren_words)

    question_numbers = list(range(0, len(eng_words)))
    #print(question_numbers)

    shuffled_list = random.sample(question_numbers, int(quiz_length))
    #print(shuffled_list)

    final_score = get_quiz(quiz_length)
    #print(final_score)
    
    print("****************************")
    print("You scored :", final_score)
    print("****************************")

    # email formatting
    subject = "French Quiz Score"

    content = f"""
    <h3>This is a test of the French Quiz Score Email Report</h3>
   
    <h4>French Quiz Score Report</h4>
    <br>
    Level: {valid_level} <br>
    Categroy: {valid_category} <br>
    <br>

    ************************** <br>
    Final Score: {final_score} out of {quiz_length} <br>
    ************************** <br>
    
    <br>
    <br>

    """

    send_email(subject, content) # uses the default email ID to send from and receive to.