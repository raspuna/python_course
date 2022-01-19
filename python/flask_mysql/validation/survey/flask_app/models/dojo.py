from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    db = 'dojo_survey_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def select_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        all_objs = []
        for obj in results:
            all_objs.append(cls(obj))
        return all_objs
    
    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result[0]
    
    @classmethod 
    def insert(cls, data):
        query = """
            INSERT INTO dojos 
            (name, location, language, comment, created_at, updated_at) 
            VALUES
            (%(name)s, %(location)s, %(language)s, %(comment)s, UTC_TIMESTAMP(), UTC_TIMESTAMP());
            """
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(survey['location']) < 2:
            flash("Location must be chosen.") 
            is_valid = False
        if len(survey['language']) < 2:
            flash("Language must be chosen.")
            is_valid = False
        if 'gender' not in survey:
            flash("Please choose gender")
            is_valid = False
        return is_valid