from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    db = 'books'
    def __init__(self, data):
        self.author_id = data['author_id']
        self.book_id = data['book_id']
    
    @classmethod
    def select_with_book(cls, data):
        query = "SELECT * FROM favorites WHERE book_id= %(book_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        obj_list =[]
        for obj in results:
            obj_list.append(cls(obj))
        return obj_list

    @classmethod
    def insert(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        row_id = connectToMySQL(cls.db).query_db(query, data)
        return row_id

    @classmethod
    def update(cls, data):
        query = "UPDATE favorites SET updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM favorites WHERE book_id = %(book_id)s AND author_id = %(author_id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return None