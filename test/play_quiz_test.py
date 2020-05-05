# test/play_quiz_test.py

import csv
import random
import os
import pytest

from app.play_quiz import level_validation, get_level_data, category_validation, get_category_data
from app.play_quiz import get_eng_word, get_fren_word

def test_level_validation():

    all_data_sample = [
    {'gender': 'F', 'french_word': 'agrafeuse', 'english_word': 'stapler', 'category': 'stationary', 'level': '1'}, 
    {'gender': 'F', 'french_word': 'regle', 'english_word': 'ruler', 'category': 'stationary', 'level': '1'}, 
    {'gender': 'M', 'french_word': 'classeur', 'english_word': 'file', 'category': 'stationary', 'level': '1'},
    {'gender': 'M', 'french_word': 'pain', 'english_word': 'bread', 'category': 'cuisine', 'level': '2'}, 
    {'gender': 'F', 'french_word': 'pomme', 'english_word': 'apple', 'category': 'cuisine', 'level': '2'}, 
    {'gender': 'M', 'french_word': 'poisson', 'english_word': 'fish', 'category': 'cuisine', 'level': '2'}
    ]
    
    user_level_sample = "1"
    count = 0

    for data in all_data_sample:
        if data["level"] == user_level_sample:
            count = count + 1
        else:
            pass
    
    if count == 0:
        result = print("You chose an invalid level, please try again"), exit()
    else:
        result = user_level_sample

    assert result == level_validation(user_level_sample, all_data_sample)

def test_get_level_data():
    
    all_data_sample = [
    {'gender': 'F', 'french_word': 'agrafeuse', 'english_word': 'stapler', 'category': 'stationary', 'level': '1'}, 
    {'gender': 'F', 'french_word': 'regle', 'english_word': 'ruler', 'category': 'stationary', 'level': '1'}, 
    {'gender': 'M', 'french_word': 'classeur', 'english_word': 'file', 'category': 'stationary', 'level': '1'},
    {'gender': 'M', 'french_word': 'pain', 'english_word': 'bread', 'category': 'cuisine', 'level': '2'}, 
    {'gender': 'F', 'french_word': 'pomme', 'english_word': 'apple', 'category': 'cuisine', 'level': '2'}, 
    {'gender': 'M', 'french_word': 'poisson', 'english_word': 'fish', 'category': 'cuisine', 'level': '2'}
    ]
    
    level_data_sample = []
    user_level_sample = "1"

    for data in all_data_sample:
        if data["level"] == user_level_sample:
            level_data_sample.append(data)
        else:
            pass
    
    result = level_data_sample

    assert result == get_level_data(user_level_sample, all_data_sample)

def test_category_validation():
    
    level_data_sample = [
    {'gender': 'F', 'french_word': 'agrafeuse', 'english_word': 'stapler', 'category': 'stationary', 'level': '1'}, 
    {'gender': 'F', 'french_word': 'regle', 'english_word': 'ruler', 'category': 'stationary', 'level': '1'}, 
    {'gender': 'M', 'french_word': 'classeur', 'english_word': 'file', 'category': 'stationary', 'level': '1'}, 
    {'gender': 'M', 'french_word': 'chien', 'english_word': 'dog', 'category': 'animals', 'level': '1'}, 
    {'gender': 'F', 'french_word': 'chat', 'english_word': 'cat', 'category': 'animals', 'level': '1'}, 
    {'gender': 'F', 'french_word': 'vache', 'english_word': 'cow', 'category': 'animals', 'level': '1'}
    ]

    user_category_sample = "animals"
    count = 0

    for data in level_data_sample:
        if data["category"] == user_category_sample:
            count = count + 1
        else:
            pass
    
    if count == 0:
        result = print("You chose an invalid category, please try again"), exit()
    else:
        result = user_category_sample
    
    assert result == category_validation(user_category_sample, level_data_sample)

def test_get_category_data():
    
    level_data_sample = [
    {'gender': 'F', 'french_word': 'agrafeuse', 'english_word': 'stapler', 'category': 'stationary', 'level': '1'}, 
    {'gender': 'F', 'french_word': 'regle', 'english_word': 'ruler', 'category': 'stationary', 'level': '1'}, 
    {'gender': 'M', 'french_word': 'classeur', 'english_word': 'file', 'category': 'stationary', 'level': '1'}, 
    {'gender': 'M', 'french_word': 'chien', 'english_word': 'dog', 'category': 'animals', 'level': '1'}, 
    {'gender': 'F', 'french_word': 'chat', 'english_word': 'cat', 'category': 'animals', 'level': '1'}, 
    {'gender': 'F', 'french_word': 'vache', 'english_word': 'cow', 'category': 'animals', 'level': '1'}
    ]
    
    category_data_sample = []
    user_category_sample = "animals"

    for data in level_data_sample:
        if data["category"] == user_category_sample:
            category_data_sample.append(data)
        else:
            pass
        
    result = category_data_sample

    assert result == get_category_data(user_category_sample, level_data_sample)

def test_get_eng_word():

    category_data_sample = [
    {'gender': 'M', 'french_word': 'pain', 'english_word': 'bread', 'category': 'cuisine', 'level': '2'}, 
    {'gender': 'F', 'french_word': 'pomme', 'english_word': 'apple', 'category': 'cuisine', 'level': '2'}, 
    {'gender': 'M', 'french_word': 'poisson', 'english_word': 'fish', 'category': 'cuisine', 'level': '2'},
    ]

    eng_words = []
    for data in category_data_sample:
        eng_word = data["english_word"]
        eng_words.append(eng_word)
    
    result = ['bread','apple','fish']

    assert get_eng_word(category_data_sample) == result

def test_get_fren_word():

    category_data_sample = [
    {'gender': 'M', 'french_word': 'pain', 'english_word': 'bread', 'category': 'cuisine', 'level': '2'}, 
    {'gender': 'F', 'french_word': 'pomme', 'english_word': 'apple', 'category': 'cuisine', 'level': '2'}, 
    {'gender': 'M', 'french_word': 'poisson', 'english_word': 'fish', 'category': 'cuisine', 'level': '2'},
    ]

    fren_words = []
    for data in category_data_sample:
        fren_word = data["french_word"]
        fren_words.append(fren_word)
    
    result = ['pain','pomme','poisson']

    assert get_fren_word(category_data_sample) == result

