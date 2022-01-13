from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import book, author, favorite

@app.route('/books')
@app.route('/books/add')
def show_books():
    return render_template("books.html", books = book.Book.select_all())

@app.route('/books/new', methods=['POST'])
def add_book():
    print(request.form)
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    book.Book.insert(data)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_book(id):
    data = { 'id': id }
    the_book = book.Book.select_one(data)
    fav_data = { 'book_id' : id }
    authors = author.Author.select_without_book(fav_data)
    fav_authors = author.Author.select_with_book(fav_data)
    return render_template("book.html", fav_authors = fav_authors, authors=authors, book = the_book)

@app.route('/books/<int:book_id>/remove')
def delete_book(book_id):
    data = { 'book_id': book_id }
    favs = favorite.Favorite.select_with_book(data)
    for fav in favs:
        d = { 
            'author_id': fav.author_id,
            'book_id' : book_id
        }
        favorite.Favorite.delete(d)
    data = { 'id': book_id}
    book.Book.delete(data)
    return redirect('/books')

