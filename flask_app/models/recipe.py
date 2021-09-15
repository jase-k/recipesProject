from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

db = 'mydb'
class Recipe:
    def __init__(self, data):
        self.name = data['name']
        self.description= data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_30= data['sub30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def addRecipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, created_at, updated_at, user_id) Values(%(name)s, %(description)s, %(instructions)s, %(date)s, %(under_30)s, NOW(), NOW(), %(user_id)s)"

        id = MySQLConnection(db).query_db(query, data)
        
        if(id):
            print('successfully added recipe to database')
            return id
        else:
            print("Didn't add to database")
            return False

    @staticmethod
    def validateRecipe(data):
        is_valid = True
        # Validates name
        if len(data['name']) < 3:
            flash('Name has to be longer than 2 characters', 'name')
            is_valid = False
        
        # Validates description
        if len(data['description']) < 1:
            flash('Must have description', 'description')
            is_valid = False
        
        # Validates instructions
        if len(data['instructions']) < 1:
            flash('Must have instructions', 'instruction')
            is_valid = False

        # Validates date_made
        if not data["date"]:
            flash('Must set Date', 'date')
            is_valid = False

        return is_valid
