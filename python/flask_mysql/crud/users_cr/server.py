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
    query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (%(f)s, %(l)s, %(e)s, NOW());"
    result = connectToMySQL('Users').query_db(query, data)   
    return redirect("/")    


if __name__ == "__main__":
    app.run(debug=True)