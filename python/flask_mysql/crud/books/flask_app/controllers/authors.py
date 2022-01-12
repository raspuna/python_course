from flask_app import app
from flask import render_template, redirect, session
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("index.html", users = User.select_all())
