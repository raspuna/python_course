from flask import Flask, render_template, session, redirect, request, url_for
import random
from datetime import date, datetime

app = Flask(__name__)
app.secret_key="?PY??<3??B?3??ht"

@app.route('/')
def index():
    welcome_msg = ["Welcome..", "Find Gold!"]
    if 'msg' not in session:
        session['msg'] = welcome_msg
    if 'gold' not in session:
        session['gold'] = 0

    return render_template("index.html", gold=session['gold'], activities=session['msg'])

@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)
    print(request.form['building'])
    building = request.form['building']
    if building == "farm":
        money = random.randrange(10,21)
    elif building == "cave":
        money = random.randrange(5,11) 
    elif building == "house":
        money = random.randrange(2,6)
    else:
        money = random.randrange(-50, 51)

    if building == "casino":
        if money < 0:
            msg = f"Entered a casino and lost {-money} gold.. Ouch.."
        elif money > 0 :
            msg = f"Entered a casino and earn {money} gold.. Yay!"
        else:
            msg = f"Entered a casino and nothing happened!"

    else:
        msg = f"earned {money} from the {building}!"
    
    msg_with_time = f"{msg} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"
    session['gold'] += money
    session['msg'].append(msg_with_time) 
    session['msg'] = session['msg'][-10:]

    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)