from flask_app import app
from flask_app.controllers import authors, books, favorites

if __name__ == "__main__":
    #app.run(debug=True)
    app.run("0.0.0.0", port="5050")