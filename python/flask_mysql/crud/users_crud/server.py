from flask import Flask, redirect, render_template, request
from mysqlconnection import connectToMySQL
from user import User

app = Flask(__name__)

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
        'f' : request.form['fname'],
        'l' : request.form['lname'],
        'e' : request.form['email']
    }
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(f)s, %(l)s, %(e)s, NOW(), NOW());"
    result = connectToMySQL('Users').query_db(query, data)   
    return redirect("/")    

@app.route("/users/<int:x>")
def show(x):
    data = {
        'userid': x
    }
    query = "SELECT * FROM USERS WHERE id = %(userid)s;"
    result = connectToMySQL('Users').query_db(query, data)
    print(result)
    userdata = result[0]
    return render_template("user.html", user = userdata)

@app.route("/users/<int:x>/edit")
def edit(x):
    print("here?")
    data = {
        'userid' : x
    }
    query = "SELECT * FROM USERS WHERE id = %(userid)s;"
    result = connectToMySQL('Users').query_db(query, data)
    userdata = result[0]
    return render_template("update.html", user = userdata)

@app.route("/users/edit", methods=['POST'])
def update_query():
    print(request.form)
    data = {
        'f' : request.form['fname'],
        'l' : request.form['lname'],
        'e' : request.form['email'],
        'id' : request.form['id']
    }
    query = "UPDATE users SET first_name = %(f)s, last_name = %(l)s, email = %(e)s, updated_at = Now() WHERE id = %(id)s;"
    result = connectToMySQL('Users').query_db(query, data)   
    return redirect(f"/users/{data['id']}")     

@app.route('/users/<int:x>/destroy')
def delete_query(x):
    data = {
        'id': x
    }
    query = "DELETE FROM users WHERE id = %(id)s;"
    connectToMySQL('Users').query_db(query, data)
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)