from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "greatnumgame"


@app.route("/")
def num_game():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    return render_template('index.html') 

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/attempts', methods=['POST'])
def attempts():
    session['attempts'] = session['guess']
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 





