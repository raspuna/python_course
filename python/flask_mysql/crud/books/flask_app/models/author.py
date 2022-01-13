from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    db = 'books'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.db).query_db(query)
        all_objs = []
        for obj in results:
            all_objs.append(cls(obj))
        return all_objs

    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        user = result[0]
        return user

    @classmethod
    def insert(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def update(cls, data):
        query = "UPDATE authors SET updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM authors WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None
    
    @classmethod
    def select_with_book(cls, data):
        query = """
            SELECT * FROM authors 
            LEFT JOIN favorites ON authors.id = favorites.author_id
            WHERE favorites.book_id = %(book_id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        all_objs = []
        for obj in results:
            all_objs.append(cls(obj))
        return all_objs
    
    @classmethod
    def select_without_book(cls, data):
        query = """
            SELECT * FROM authors
            WHERE id NOT IN
			(SELECT A.id FROM authors A
            JOIN favorites ON A.id = favorites.author_id
            WHERE favorites.book_id = %(book_id)s )
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        all_objs = []
        for obj in results:
            all_objs.append(cls(obj))
        return all_objs