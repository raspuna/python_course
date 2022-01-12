from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninja():
    return render_template("ninjas.html", dojos=Dojo.select_all())

@app.route("/ninjas/new", methods=['POST'])
def add_ninja():
    print(request.form)
    data = {
        'first_name' : request.form['fname'],
        'last_name' : request.form['lname'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo']
    }
    Ninja.insert(data)
    return redirect(f"/dojos/{data['dojo_id']}")
