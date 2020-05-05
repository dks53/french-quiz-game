# Darshil's french-quiz-game
OPIM 244 Final Project

This document walks you (the user) through this french quiz game. It will help you setup your environment to run the code successfully. 

## What does this code do?

text goes here

## If you want to create this program on your own, here's what you can do:

## Installation

Fork the repository from GitHub [source](https://github.com/dks53/french-quiz-game.git). 

Then use GitHub Desktop software or the command-line to download or "clone" the repository onto your computer. 

Choose a familiar download location like the Desktop.


```sh
git clone https://github.com/YOUR_USERNAME/french-quiz-game.git # this is the HTTP address, but you could altenatively use the SSH address
```

## Setup

After cloning the repo, navigate there from the command-line: 

```sh
cd ~/Desktop/robo-advisor/app
```

## Prerequisits

Create a new ".env" file in your repository.

### Email API

Sign up for a free account at: https://signup.sendgrid.com/
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

## Usage

Once you have the entire program set-up, from within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python app/play_quiz.py
```

Run a local web server, then view your app in a browser at http://localhost:5000/:

```sh
FLASK_APP=web_app flask run
```

> NOTE: you can quit the server by pressing ctrl+c at any time. If you change a file, you'll likely need to restart the server for the changes to take effect.

## Deploying

First, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), and make sure you can login and list your applications. Then create a new application server, optionally specifying a name (e.g. "french-quiz-web-app"):

```sh
heroku login

heroku apps:list
heroku apps:create french-quiz-web-app # or do this from the online console
heroku apps:list
```

Then associate this repository with that application, as necessary:

```sh
git remote -v
heroku git:remote -a french-quiz-web-app # necessary if you created the app from the online console
git remote -v
```

After this configuration process is complete, you should be able to "deploy" the application's source code to the Heroku server:

```
git push heroku master
```
