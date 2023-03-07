from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] +=1
    return render_template('counter.html')

@app.route('/count', methods=['POST'])
def add_to_count():
    if request.form["change"]=="add2":
        session["count"] +=1
    elif request.form["change"]=="reset":
        session["count"] = 0

    return redirect("/")

@app.route('/destory_session')
def end_session():
    session.clear()
    return redirect ('/')




if __name__ =="__main__":
    app.run(debug=True)






