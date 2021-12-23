from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "?PY??<3??B?3??h"

@app.route("/")
def index():
    if 'visit' not in session:
        session['visit'] = 1
    else:
        session['visit'] += 1
    if 'cnt' not in session:
        session['cnt'] = 0
    return render_template("counter.html", cnt=session['cnt'], visit=session['visit'])

@app.route("/count", methods=['POST'])
def count():
    print(request.form)
    if 'add_num' in request.form:
        if request.form['num']:
            session['cnt'] += int(request.form['num'])
    else:
        session['cnt'] += 2
    session['visit'] -= 1
    return redirect("/")


@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)