from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, language, user_language
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
@app.route('/')
def index():
    if session and '_flashes' not in session:
        print('session', session)
        return redirect('/welcome')
    return render_template("index.html", states = STATES, languages = language.Language.select_all())

@app.route('/register', methods=['POST'])
def register_user():
    if not user.User.validate(request.form):
        return redirect('/')
    
    data = {}
    user_langs = []
    for key, val in request.form.items():
        if key == 'password':
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
            data[key] = pw_hash
        elif key == 'confirm_password':
            continue
        elif len(key) > 8 and key[0:8] == 'language':
            user_langs.append(key[8:])
        else:
            data[key] = val
    
    if not user_langs :
        flash("Required at leat 1 language", category='register')
        return redirect('/')

    user_id = user.User.insert(data)
    session['user_id'] = user_id
    session['first_name'] = data['first_name']
    session['last_name'] = data['last_name']

    for lang in user_langs:
        data = {
            'user_id' : user_id,
            'language_id' : int(lang)
        }
        user_language.UserHasLanguage.insert(data)
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    if not session:
        return redirect('/')
    username = f"{session['first_name']} {session['last_name']}"
    return render_template('welcome.html', username = username) 

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
    }
    the_user = user.User.select_by_email(data)
    if not the_user:
        flash('Invalid Email/Password', category='login')
        return redirect('/')
    print(the_user)
    if not bcrypt.check_password_hash(the_user.password, request.form['password']):
        flash('Invalid Email/Password', category='login')
        return redirect('/')
    session['user_id'] = the_user.id
    session['first_name'] = the_user.first_name
    session['last_name'] = the_user.last_name
    return redirect('/welcome')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
