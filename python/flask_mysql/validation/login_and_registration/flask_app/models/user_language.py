from flask_app.config.mysqlconnection import connectToMySQL

class UserHasLanguage:
    db = 'login_registration'
    def __init__(self, data):
        self.user_id = data['user_id']
        self.language_id = data['language_id']
    
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
        query = "INSERT INTO users_has_languages (user_id, language_id) VALUES (%(user_id)s, %(language_id)s);"
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM user_has_languages WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None