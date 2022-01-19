from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models import dojo

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def new_survey():
    data = {}
    for key, val in request.form.items():
        data[key] = val
        session[key] = val
    print(session)
    if not dojo.Dojo.validate_survey(request.form):
        print("hey?")
        return redirect('/')
    session['id'] = dojo.Dojo.insert(data)
    return redirect('/result')

@app.route('/result')
def show_result():
    data = {
        'id' : session['id']
    }
    result = dojo.Dojo.select_one(data)
    return render_template("result.html", data=result)

@app.route("/reset", methods=['POST'])
def reset():
    session.clear()
    return redirect("/")

@app.route("/goback", methods=['POST'])
def goback():
    return redirect("/")
