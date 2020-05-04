# Darshil's french-quiz-game
OPIM 244 Final Project

This document walks you (the user) through this french quiz game. It will help you setup your environment to run the code successfully. 

## What does this code do?

This is a financial planning business which helps customers make investment decisions.

This is an automated tool that is built to provide you with stock trading recommendations.

Specifically, the system accepts one or more stock symbols as information inputs, then it requests real live historical trading data from the internet, and finally provides a recommendation as to whether or not you should purchase the given stock(s).

## If you want to create this program on your own, here's what you can do:

## Setup
Use GitHub Desktop software or the command-line to download or "clone" the repository onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line: 

```sh
cd ~/Desktop/robo-advisor/app
```

## Prerequisits

First, create a new ".env" file in your repository.

### Email API

First, sign up for a free account at: https://signup.sendgrid.com/
Then click the link in a confirmation email to verify your account. 
Then create an API Key with "full access" permissions at: https://app.sendgrid.com/settings/api_keys

Store the API Key value in an environment variable called SENDGRID_API_KEY. Also set an environment variable called MY_EMAIL_ADDRESS to be the email address you just associated with your SendGrid account (e.g. "abc123@gmail.com").

```sh
SENDGRID_API_KEY = "________(Your API key)________" 
MY_EMAIL_ADDRESS = "________(Your email address)________" 
```

## Environment setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n french-quiz-game-env python=3.7 # (first time only)
conda activate french-quiz-game-env
```

From within the virtual environment, install the required packages specified in the "requirements.txt"

```sh
pip install -r requirements.txt
```

Once you have the entire program set-up, from within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python app/robo-advisor.py
```
