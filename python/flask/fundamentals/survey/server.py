from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "?PY??<3??B?3??h"

@app.route("/")
def survey():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def result():
    dataset = {}
    print(request.form)
    for key, val in request.form.items():
        dataset[key] = val
        session[key] = val
    print(dataset)
    return render_template("result.html", data=dataset)

@app.route("/reset", methods=['POST'])
def reset():
    session.clear()
    return redirect("/")

@app.route("/goback", methods=['POST'])
def goback():
    return redirect("/")


if __name__ == "__main__" :
    app.run(debug=True)