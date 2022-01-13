from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import author, book

@app.route('/')
@app.route('/authors')
def index():
    a = author.Author.select_all()
    print(a[0])
    return render_template("index.html", authors = a)

@app.route('/authors/new', methods=['POST'])
def add_author():
    data = {
        'name': request.form['name']
    }
    author.Author.insert(data)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_author(id):
    data = { 'id': id }
    a = author.Author.select_one(data)
    fav_data = { 'author_id' : id}
    b = book.Book.select_without_author(fav_data)
    fav_books = book.Book.select_with_author(fav_data)
    return render_template("author.html", fav_books=fav_books, author=a, books=b)