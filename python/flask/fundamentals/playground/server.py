from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome??"

@app.route("/html")
def index():
    return render_template("index.html")

@app.route("/play", defaults={'x':3, 'boxcolor':'blue'})
@app.route("/play/<int:x>", defaults={'boxcolor':'blue'})
@app.route("/play/<int:x>/<string:boxcolor>")
def play(x, boxcolor):
    print(x,boxcolor)
    return render_template("playground.html", num=x, color=boxcolor)

if __name__ == "__main__":
    app.run(debug=True)