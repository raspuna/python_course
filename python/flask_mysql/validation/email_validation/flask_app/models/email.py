from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-z]+$')
class Email:
    db = 'email_validation'
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        all_objs = []
        for obj in results:
            all_objs.append(cls(obj))
        return all_objs

    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM emails WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        user = result[0]
        return user
    @classmethod
    def select_count_email(cls, data):
        query = "SELECT count(*) as cnt FROM emails WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result[0])
        return result[0] 

    @classmethod
    def insert(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def update(cls, data):
        query = "UPDATE emails SET updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None
    
    @staticmethod
    def validate(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email address!")
            return is_valid

        e = Email.select_count_email(data)
        if e['cnt'] > 0:
            is_valid = False
            flash("Not unique email address")
        
        return is_valid

