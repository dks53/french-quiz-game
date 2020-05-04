# test/play_quiz_test.py

import csv
import random
import os
import pytest

from app.play_quiz import get_eng_word

def test_get_eng_word():

    category_data_sample = [
    {'gender': 'M', 'french_word': 'pain', 'english_word': 'bread', 'category': 'cuisine', 'level': '2'}, 
    {'gender': 'F', 'french_word': 'pomme', 'english_word': 'apple', 'category': 'cuisine', 'level': '2'}, 
    {'gender': 'M', 'french_word': 'poisson', 'english_word': 'fish', 'category': 'cuisine', 'level': '2'},\
    ]

    eng_words = []
    for data in category_data_sample:
        eng_word = data["english_word"]
        eng_words.append(eng_word)
    
    result = ['bread','apple','fish']

    assert get_eng_word(category_data_sample) == result