from tkinter import E
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    data = {
        'email': request.form['email']
    }
    if not email.Email.validate(data):
        return redirect('/')

    email.Email.insert(data)
    session['email'] = data['email']

    return redirect('/success')

@app.route('/success')
def success():
    emails = email.Email.select_all()
    return render_template("result.html", input_email = session['email'], emails = emails, is_delete = False)

@app.route('/destroy/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    input_email = email.Email.select_one(data)
    email.Email.delete(data)
    emails = email.Email.select_all()
    return render_template("result.html", input_email = input_email, emails = emails, is_delete = True)