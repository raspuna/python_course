from flask import Flask, render_template, session, redirect, request, url_for
import random
from datetime import date, datetime

app = Flask(__name__)
app.secret_key="?PY??<3??B?3??ht"

@app.route('/')
def index():
    welcome_msg = ["Welcome..", "Find Gold!"]
    msg_color = ["black", "black"]
    if 'msg' not in session:
        session['msg'] = welcome_msg
        session['color'] = msg_color
    if 'gold' not in session:
        session['gold'] = 0
    if 'move' not in session:
        session['move'] = 0

    return render_template("index.html", gold=session['gold'], activities=enumerate(session['msg']), colors=session['color'], move= session['move'])

rand = { "farm": (10, 21), "cave": (5,11), "house":(2,6), "casino":(-50,51)}
@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)
    print(request.form['building'])
    building = request.form['building']
    money_color= "blue"
    money = random.randrange(rand[building][0], rand[building][1])

    if building == "casino":
        if money < 0:
            money_color = "red"
            msg = f"Entered a casino and lost {-money} gold.. Ouch.."
        elif money > 0 :
            msg = f"Entered a casino and earn {money} gold.. Yay!"
        else:
            money_color="black"
            msg = f"Entered a casino and nothing happened!"

    else:
        msg = f"earned {money} from the {building}!"
    
    msg_with_time = f"{msg} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"
    
    session['gold'] += money
    session['msg'] = [ msg_with_time ] + session['msg'][:19]
    session['color'] = [ money_color ] + session['color'][:19]
    session['move'] += 1

    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)