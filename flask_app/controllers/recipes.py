from flask.helpers import flash
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/users/<int:id>/create_recipe')
def createRecipe(id):
    user = User.getUserbyId(id)
    return render_template('add_recipe.html', user = user)


@app.route('/add_recipe', methods=["POST"])
def addRecipe():
    print("RECIPE INFO: ", request.form)

    if not 'sub30' in request.form:
        flash('Must choose an option', 'sub30')
        return redirect(f'/users/{request.form["user_id"]}/create_recipe')

    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date' : request.form['date'],
        'under_30': request.form['sub30'],
        'user_id': request.form['user_id']
    }

    if data['under_30'] == 'True':
        data['under_30'] = True
    else:
        data['under_30'] = False

    if Recipe.validateRecipe(data):
        id = Recipe.addRecipe(data)
        return redirect(f'/users/{data["user_id"]}')

    return redirect(f'/users/{data["user_id"]}/create_recipe')