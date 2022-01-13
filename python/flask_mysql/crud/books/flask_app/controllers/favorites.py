from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import favorite

@app.route('/favorite', methods=['POST'])
def add_favorite():
    print(request.form)
    data = {
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id']
    }
    redirect_to = request.form['redirect_to']
    favorite.Favorite.insert(data)
    return redirect(f"/{redirect_to}")