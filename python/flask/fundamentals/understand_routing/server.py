from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    return f"Hello, {name}!"

@app.route('/repeat/<int:num>/<string:val>')
def repeat(num, val):
    result = val + "<br>" 
    return f"{result * num}"

@app.errorhandler(404)
def invalid(error):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)