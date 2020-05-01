# app/play_quiz.py

import csv
import random
import os

def load_database():
    #csv_file_path = "words_database.csv" # a relative filepath
    csv_file_path = os.path.join(os.path.dirname(__file__), "../data", "words_database.csv")
    all_data = [] # list containing all data from the database

    with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
        reader = csv.DictReader(csv_file) # assuming your CSV has headers
        # reader = csv.reader(csv_file) # if your CSV doesn't have headers
        for row in reader:
            #print(row["gender"], row["french_word"], row["english_word"], row["category"], row["level"])
            all_data.append(row)

    return all_data

def level_validation(user_level):
    count = 0
    for data in all_data:
        if data["level"] == user_level:
            count = count + 1
        else:
            pass
    
    if count == 0:
        return print("You chose an invalid level, please try again"), exit()
    else:
        return user_level

def get_level_data(user_level):
    level_data = []

    for data in all_data:
        if data["level"] == user_level:
            level_data.append(data)
        else:
            pass
    
    return level_data

def category_validation(user_category):
    count = 0
    for data in level_data:
        if data["category"] == user_category:
            count = count + 1
        else:
            pass
    
    if count == 0:
        return print("You chose an invalid category, please try again"), exit()
    else:
        return user_category

def get_category_data(user_category):
    category_data = []
    for data in level_data:
        if data["category"] == user_category:
            category_data.append(data)
        else:
            pass
        
    return category_data

def get_eng_word(category_data):
    eng_words = []
    for data in category_data:
        eng_word = data["english_word"]
        eng_words.append(eng_word)
    
    return eng_words

def get_fren_word(category_data):
    fren_words = []
    for data in category_data:
        fren_word = data["french_word"]
        fren_words.append(fren_word)
    
    return fren_words

def get_quiz(quiz_length):
    
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

#################
if __name__ == "__main__":

    all_data = load_database()

    chosen_level = input("Choose a level: ")
    valid_level = level_validation(chosen_level)
    print("You chose Level ", valid_level, "\n")

    level_data = get_level_data(chosen_level)
    #print(level_data)

    chosen_category = input("Choose a category: ")
    valid_category = category_validation(chosen_category)
    print("You chose the ", valid_category, "category", "\n")
    
    category_data = get_category_data(chosen_category)
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
    print("****************************")
    print("You scored :", final_score)
    print("****************************")

    #TODO: Congratulations, that's a new high score!
    #TODO: Congratulations, you answered all correctly!

    #TODO: Email report