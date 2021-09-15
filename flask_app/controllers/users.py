from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User


@app.route('/')
def mainPage():
    return render_template('login.html')

@app.route('/register', methods=["POST"])
def registerNewUser():
    #call User model to input new user in database redirect to users/id
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'], 
        "email" : request.form['email'], 
        "password" : request.form['password1'], 
        "confirm_password" : request.form['password2'],
    }
    session['first_name'] = data["first_name"]
    session['last_name'] = data["last_name"]
    session['email'] = data["email"]

    print("Form Data", data)
    id = User.insertNewUser(data)

    return redirect(f'/users/{id}')

@app.route('/login', methods=["POST"])
def loginUser():
    #match email and password to user in the database and redirect to users/id
    return "User should go to user dashboard"

@app.route('/users/<int:id>')
def userDashboard(id):
    #Display user's recipes with options to logout, view more, create a new one , view instrutions, edit or delete
    return "THis is the user dashboard"