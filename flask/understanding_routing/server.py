from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html", phrase = "hello", times=5 )

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print(name)
    return f"Hi, {name} !"

@app.route('/repeat/<int:num>/<string:username>')
def repeat(username, num):
    print(username)
    print(id)
    return f"Hello {username * num}"

@app.errorhandler(404)
def error(e):
    return 'Sorry! No response. Try Again.'

if __name__ =="__main__":
    app.run(debug=True)





