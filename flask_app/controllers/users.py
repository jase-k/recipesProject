from flask_app import app
from flask import render_template, redirect, request


@app.route('/')
def mainPage():
    return render_template('main.html')