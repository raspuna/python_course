from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome??"

@app.route("/html")
def index():
    return render_template("index.html")