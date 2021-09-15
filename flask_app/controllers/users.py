from flask_app import app
from flask import render_template, redirect, request


@app.route('/')
def mainPage():
    return render_template('login.html')

@app.route('/register')
def registerNewUser():
    return "New user should be added"

@app.route('/login')
def loginUser():
    return "User should go to user dashboard"