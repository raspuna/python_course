from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import recipe,user

@app.route('/recipes/<int:recipe_id>')
def view_recipe(recipe_id):
    if 'user_id' not in session:
        print('wrong access', session)
        return redirect('/')
    data = {
        'id': recipe_id
    }
    the_recipe = recipe.Recipe.select_one(data)
    if not the_recipe:
        return redirect('/dashboard')
    if session['user_id'] == the_recipe.user_id:
        is_author = True
    else:
        is_author = False
    description = the_recipe.description.split("\r\n")
    instructions = the_recipe.instructions.split("\r\n")
    the_user = user.User.select_one({'id':session['user_id']})
    return render_template("recipe.html", recipe = the_recipe, user=the_user,\
            is_author = is_author,\
            description=description, instructions = instructions)

@app.route('/recipes/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        print('wrong access', session)
        return redirect('/')
    data = {
        'id': recipe_id
    }
    the_recipe = recipe.Recipe.select_one(data)
    if not the_recipe:
        return redirect('/dashboard')
    if session['user_id'] != the_recipe.user_id:
        return redirect('/dashboard')
    else:
        the_user = user.User.select_one({'id':session['user_id']})
        return render_template("edit_recipe.html", recipe = the_recipe, user=the_user)

@app.route('/recipes/update', methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        print('wrong access', session)
        return redirect('/')
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/edit/{request.form['id']}")
    data = {}
    for key, val in request.form.items():
        data[key] = val
    print(data)
    data['user_id'] = session['user_id']
    recipe.Recipe.update(data) 
    return redirect(f"/recipes/{data['id']}")

@app.route('/recipes/new_recipe')
def new_recipe():
    if 'user_id' not in session:
        print('wrong access', session)
        return redirect('/')
    the_user = user.User.select_one({'id':session['user_id']})
    return render_template("new_recipe.html",user=the_user)


@app.route('/recipes/add', methods=['POST'])
def insert_recipe():
    if 'user_id' not in session:
        print('wrong access', session)
        return redirect('/')
    if not recipe.Recipe.validate_recipe(request.form):
        print("error!")
        return redirect("/recipes/new_recipe")

    data = {}
    for key, val in request.form.items():
        data[key] = val
    print(data)
    data['user_id'] = session['user_id']
    rowid = recipe.Recipe.insert(data) 
    return redirect(f"/recipes/{rowid}")

@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    if 'user_id' not in session:
        print('wrong access', session)
        return redirect('/')
    data = {
        'id': recipe_id
    }
    the_recipe = recipe.Recipe.select_one(data)
    if not the_recipe:
        return redirect('/dashboard')
    if session['user_id'] != the_recipe.user_id:
        flash("Wrong Access")
        return redirect('/dashboard')
    else:
        recipe.Recipe.delete(data)
    return redirect('/dashboard')



