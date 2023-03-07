from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "gimmedaloot"


@app.route("/")
def start():

    if "gold_count" not in session:
        session["gold_count"] = 0
    elif session["gold_count"] >= 500:
        session['gold_count'] = '<p class="alert alert-success">Congrats You won with %s gold.</p>'%(str(session["gold_count"])) 

    if "act_log" not in session:
        session["act_log"] = []

    act_log = session["act_log"]
    gold_count = session["gold_count"]
    return render_template("ninja_gold.html", act_log = reversed(act_log), gold_count = gold_count)
@app.route("/process_money", methods=["POST"])
def get_gold():
    
    if request.form['building'] == 'farm':
        gold_amount = random.randint(10,20)
        session['gold_count'] += gold_amount
        time = datetime.datetime.now()
        event = '<p class="alert alert-success">You had earned %s gold from your farm.(%s)</p>'%(str(gold_amount),time)
        session['act_log'].append(event)
    
    elif request.form['building'] == 'cave':
        gold_amount = random.randint(5,10)
        session['gold_count'] += gold_amount
        time = datetime.datetime.now()
        event = '<p class="alert alert-success">You had earned %s gold from your cave.(%s)</p>'%(str(gold_amount),time)
        session['act_log'].append(event)

    elif request.form['building'] == 'house':
        gold_amount = random.randint(2,5)
        session['gold_count'] += gold_amount
        time = datetime.datetime.now()
        event = '<p class="alert alert-success">You had earned %s gold from your house.(%s)</p>'%(str(gold_amount),time)
        session['act_log'].append(event)

    if request.form['building'] == 'casino':
        gold_amount = random.randint(-50,50)
        session['gold_count'] += gold_amount
        if gold_amount > int(1):
            time = datetime.datetime.now()
            event = '<p class="alert alert-success">Big winner at the casino with %s gold!!(%s)</p>'%(str(gold_amount),time)
            session['act_log'].append(event)
        elif gold_amount< int(1):
            time = datetime.datetime.now()
            event = '<p class="alert alert-danger">Maybe try your luck elsewhere you lost %s gold at the casino... Ouch!(%s)</p>'%(str(gold_amount),time)
            session['act_log'].append(event)


    return redirect("/")

@app.route("/restart")
def restart_game():
    session.clear()
    return redirect("/")




if __name__=="__main__":
    
    app.run(debug=True) 