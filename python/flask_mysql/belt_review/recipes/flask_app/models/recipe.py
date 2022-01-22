from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

ATTR_LIST = ['name', 'cook_time', 'description', 'instructions', 'date_made']
class Recipe:
    db = 'recipes_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cook_time = data['cook_time']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db).query_db(query)
        all_objs = []
        for obj in results:
            all_objs.append(cls(obj))
        return all_objs

    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None

    @classmethod
    def insert(cls, data):
        query = """
        INSERT INTO recipes 
        (name, cook_time, description, instructions, date_made, 
        user_id,
        created_at, updated_at) 
        VALUES 
        (%(name)s, %(cook_time)s, %(description)s, %(instructions)s, %(date_made)s,
        %(user_id)s,
        NOW(), NOW()); 
        """
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def update(cls, data):
        query = """
        UPDATE recipes SET 
        name = %(name)s, cook_time = %(cook_time)s, 
        description = %(description)s, instructions = %(instructions)s, 
        date_made = %(date_made)s,
        updated_at = NOW() WHERE id = %(id)s;"""
        connectToMySQL(cls.db).query_db(query, data)
        return None

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None
    
    @staticmethod
    def validate_recipe(recipe):
        print("validate_recipe:", recipe)
        for attr in ATTR_LIST:
            print("test", attr)
            if attr not in recipe or len(recipe[attr]) < 1:
                flash(f"{attr} is missing.")
                return False
        if len(recipe['name']) < 3:
            flash("name is too short. It should be at least 3 characters.")
            return False
        if len(recipe['description']) < 3:
            flash("description is too short. It should be at least 3 characters.")
            return False
        if len(recipe['instructions']) < 3:
            flash("Instruction is too short. It should be at least 3 characters.")
            return False
        return True
    