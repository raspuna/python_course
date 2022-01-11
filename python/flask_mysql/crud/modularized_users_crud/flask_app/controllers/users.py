from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route("/")
@app.route("/users")
def users():
    all_users = User.get_all()
    return render_template("index.html", all_users = all_users)

@app.route("/users/new")
def add_user():
    return render_template("add.html")

@app.route("/users/run", methods=['POST'])
def insert_query():
    print(request.form)
    data = {
        'first_name' : request.form['fname'],
        'last_name' : request.form['lname'],
        'email' : request.form['email']
    }
    User.insert(data)
    return redirect("/")    

@app.route("/users/<int:x>")
def show(x):
    data = {
        'id': x
    }
    return render_template("user.html", user = User.get_one(data))

@app.route("/users/<int:x>/edit")
def edit(x):
    data = {
        'id' : x
    }
    return render_template("update.html", user = User.get_one(data))

@app.route("/users/edit", methods=['POST'])
def update_query():
    print(request.form)
    data = {
        'first_name' : request.form['fname'],
        'last_name' : request.form['lname'],
        'email' : request.form['email'],
        'id' : request.form['id']
    }
    User.update(data)
    return redirect(f"/users/{data['id']}")     

@app.route('/users/<int:x>/destroy')
def delete_query(x):
    data = {
        'id': x
    }
    User.delete(data)
    return redirect("/")