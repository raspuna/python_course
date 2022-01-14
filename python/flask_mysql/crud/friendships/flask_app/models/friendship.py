from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Friendship:
    db = 'friendships_schema'
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def select_all(cls):
        query = """
            SELECT u.first_name AS user_fname, u.last_name AS user_lname, f.first_name AS friend_fname, f.last_name AS friend_lname FROM users u 
            JOIN friendships ON u.id = friendships.user_id 
            JOIN users f ON friendships.friend_id = f.id;
        """
        results = connectToMySQL(cls.db).query_db(query)
        all_objs = []
        for obj in results:
            print(obj)
            all_objs.append(obj)
        return all_objs

    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM friendships WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        user = result[0]
        return user

    @classmethod
    def insert(cls, data):
        query = "INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES (%(user_id)s, %(friend_id)s, NOW(), NOW());"
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def update(cls, data):
        query = "UPDATE friendships SET first_name=%(first_name)s, last_name=%(last_name)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM friendships WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None