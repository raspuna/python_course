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
    if not User.validate_register(request.form):
        return redirect('/')
    
    data = {}
    for key, val in request.form.items():
        if key == 'password':
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
            data[key] = pw_hash
        elif key == 'confirm_password':
            continue
        else:
            data[key] = val
    
    user_id = User.insert(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/myaccount')
def edit_user():
    data = { 'id': session['user_id'] }
    the_user = User.select_one(data)
    if not the_user:
        flash('Something went wrong', category='login')
        return redirect('/')
    return render_template("edit_user.html", user=the_user)

@app.route('/users/update', methods=['POST'])
def update_user():
    data ={ 'id': session['user_id']}
    the_user = User.select_one(data)
    if not the_user:
        flash('Something went wrong', category='login')
        return redirect('/')
    if not bcrypt.check_password_hash(the_user.password, request.form['password']):
        flash('Invalid Password', category='edituser')
        return redirect('/myaccount')
    if not User.validate_userinfo(request.form, category='edituser'):
        return redirect('/myaccount')

    for key, val in request.form.items():
        data[key] = val
    User.update(data)
    return redirect('/myaccount')

@app.route('/users/change_password', methods=['POST'])
def change_password():
    data ={ 'id': session['user_id']}
    the_user = User.select_one(data)
    if not the_user:
        flash('Something went wrong', category='login')
        return redirect('/')
    if not bcrypt.check_password_hash(the_user.password, request.form['old_password']):
        flash('Invalid Password', category='password')
        return redirect('/myaccount')
    data['password'] = request.form['new_password']
    data['confirm_password'] = request.form['confirm_password']
    if not User.validate_password(data, category='password'):
        return redirect('/myaccount')
    data['password'] = bcrypt.generate_password_hash(data['password'])
    User.update_password(data)
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if not session:
        return redirect('/')
    data ={ 'id': session['user_id']}
    the_user = User.select_one(data)
    return render_template('dashboard.html', user=the_user,\
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
    if not bcrypt.check_password_hash(the_user.password, request.form['password']):
        flash('Invalid Email/Password', category='login')
        return redirect('/')
    session['user_id'] = the_user.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
