from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

class User:
    db = 'recipes_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        all_objs = []
        for obj in results:
            all_objs.append(cls(obj))
        return all_objs

    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        user = result[0]
        return user

    @classmethod
    def select_count_by_email(cls, data):
        query = "SELECT count(*) as cnt FROM users WHERE email= %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        cnt = result[0]['cnt']
        return cnt

    @classmethod
    def select_by_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None

    @classmethod
    def insert(cls, data):
        query = """
        INSERT INTO users 
        (first_name, last_name, email, password, 
        created_at, updated_at) 
        VALUES 
        (%(first_name)s, %(last_name)s, %(email)s, %(password)s, 
        NOW(), NOW()); 
        """
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None
    
    @staticmethod
    def validate(user):
        print(user)
        if len(user['first_name']) < 2:
            flash("First name is too short", category='register')
            return False
        if not USERNAME_REGEX.match(user['first_name']):
            flash("First name is Invalid", category='register')
            return False
        if len(user['last_name']) < 2:
            flash("Last name is too short", category='register')
            return False    
        if not USERNAME_REGEX.match(user['last_name']):
            flash("Last name is Invalid", category='register')
            return False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address", category='register')
            return False
        cnt = User.select_count_by_email(user)
        if cnt > 0:
            flash("Not unique email address", category='register')
            return False
        if len(user['password']) < 8:
            flash("password is too short", category='register')
            return False
        if not PASSWD_REGEX1.match(user['password']) or not PASSWD_REGEX2.match(user['password']):
            flash("Password must have least 1 Upper case letter and 1 number", category='register')
            return False
        if user['password'] != user['confirm_password']:
            flash("password does not match", category='register')
            return False

        return True

USERNAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-z]+$')
PASSWD_REGEX1 = re.compile(r'.*[A-Z]+.*')
PASSWD_REGEX2 = re.compile(r'.*[0-9]+.*')