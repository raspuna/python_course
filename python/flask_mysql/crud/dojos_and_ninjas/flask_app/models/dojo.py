from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    db = 'dojos_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        all_user = []
        for el in results:
            all_user.append(cls(el))
        return all_user

    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        user = result[0]
        return user

    @classmethod
    def insert(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None