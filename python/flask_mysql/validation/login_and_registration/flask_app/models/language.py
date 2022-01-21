from flask_app.config.mysqlconnection import connectToMySQL

class Language:
    db = 'login_registration'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
    
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM languages;"
        results = connectToMySQL(cls.db).query_db(query)
        all_objs = []
        for obj in results:
            all_objs.append(cls(obj))
        return all_objs

    @classmethod
    def insert(cls, data):
        query = "INSERT INTO languages (name) VALUES (%(name)s);"
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM languages WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None