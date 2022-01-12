from flask_app import app
from flask_app.controllers import ninjas
from flask_app.controllers import dojos

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5050)
    app.run(debug=True)