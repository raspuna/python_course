from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'dojos_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.db).query_db(query)
        all_user = []
        for el in results:
            all_user.append(cls(el))
        return all_user

    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        user = result[0]
        return user
    
    @classmethod
    def select_dojo(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        all_ninjas = []
        for ninja in results:
            all_ninjas.append(cls(ninja))
        return all_ninjas


    @classmethod
    def insert(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None