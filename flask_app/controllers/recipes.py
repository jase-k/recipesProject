from flask.globals import session
from flask.helpers import flash
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/users/<int:id>/create_recipe')
def createRecipe(id):
    user = User.getUserbyId(id)
    return render_template('add_recipe.html', user = user, recipe = '')


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

@app.route('/recipes/<int:id>/view')
def viewRecipe(id):
    recipe = Recipe.getRecipe(id)
    user = User.getUserbyId(session["id"])

    return render_template('recipe_instructions.html', recipe= recipe, user = user)


@app.route('/recipes/<int:id>/edit')
def editRecipe(id):
    recipe = Recipe.getRecipe(id)
    user = User.getUserbyId(recipe.user_id)

    return render_template('add_recipe.html', recipe = recipe, user = user)

@app.route('/edit_recipe', methods =["POST"])
def updateRecipe():
    data = {
        "id" : request.form['id'],
        "name" : request.form['name'],
        "description": request.form['description'],
        "instructions" : request.form['instructions'],
        "date" : request.form['date'],
        "under_30": request.form['sub30'],
        "user_id": request.form['user_id']
    }
    print(data)
    recipe = Recipe.getRecipe(data['id'])
    recipe.update(data)

    return redirect(f"/users/{data['user_id']}")


@app.route('/delete_recipe/<int:id>')
def deleteRecipe(id):
    recipe = Recipe.getRecipe(id)
    recipe.delete()
    return redirect(f"/users/{recipe.user_id}")


    