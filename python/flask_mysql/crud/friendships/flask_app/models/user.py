from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = 'friendships_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
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
    def insert(cls, data):
        query = "INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None