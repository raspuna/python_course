from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models import recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if session and '_flashes' not in session:
        print('session', session)
        return redirect('/dashboard')
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register_user():
    if not User.validate(request.form):
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
    
    user_id = User.insert(data)
    session['user_id'] = user_id
    session['username'] = f"{data['first_name']} {data['last_name']}"
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if not session:
        return redirect('/')
    return render_template('dashboard.html', username = session['username'], user_id = session['user_id'], \
        is_dashboard=True, recipes=recipe.Recipe.select_all()) 

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
    }
    the_user = User.select_by_email(data)
    if not the_user:
        flash('Invalid Email/Password', category='login')
        return redirect('/')
    print(the_user)
    if not bcrypt.check_password_hash(the_user.password, request.form['password']):
        flash('Invalid Email/Password', category='login')
        return redirect('/')
    session['user_id'] = the_user.id
    session['username'] = f"{the_user.first_name} {the_user.last_name}"
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
