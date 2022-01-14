from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, friendship

@app.route('/')
def index():

    return render_template("index.html", users = user.User.select_all(), friendships = friendship.Friendship.select_all())

@app.route('/users/new', methods=['POST'])
def add_user():
    data = {
        'first_name': request.form['fname'],
        'last_name' : request.form['lname']
    }
    user.User.insert(data)
    return redirect("/")

@app.route('/friendships/new', methods=['POST'])
def add_friendship():
    data = {
        'user_id' : request.form['user_id'],
        'friend_id' : request.form['friend_id']
    }
    friendship.Friendship.insert(data)
    return redirect("/")

