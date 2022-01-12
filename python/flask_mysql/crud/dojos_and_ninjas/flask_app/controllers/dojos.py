from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
@app.route('/dojos')
def index():
    return render_template("index.html", dojos = Dojo.select_all())

@app.route('/dojos/new', methods=['POST'])
def add_dojo():
    print(request.form)
    data = {
        'name' : request.form['dojoname']
    }
    Dojo.insert(data)
    return redirect("/")

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        'id' : id
    }
    dojo = Dojo.select_one(data)
    ninjas = Ninja.select_dojo(data)
    return render_template("dojo.html", dojo = dojo, ninjas = ninjas)