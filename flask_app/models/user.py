from flask_app.config.mysqlconnection import MySQLConnection
import bcrypt

db = 'mydb'
class User: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.recipes = []

    @classmethod
    def insertNewUser(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
        data['password'] = cls.encryptPassword(data['password'])

        id = MySQLConnection(db).query_db(query, data)
        
        return id
    
    @classmethod
    def encryptPassword(cls, password):
        #Will return encrypted password via bcrypt
        
        hashed =bcrypt.hashpw(bytes(password, "utf8"), bcrypt.gensalt(14))
        return hashed