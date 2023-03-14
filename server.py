from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)
@app.route("/")
def index():
    user = User.get_all()
    print(user)
    return render_template("show_all.html", users = user)

@app.route("/create")
def create():
    return render_template("create_user.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "created_at" : request.form["created_at"]
    }
    User.save(data)
    return redirect('/')

@app.route('/users')
def show_users():
    users=User.get_all()
    return render_template("show_all.html",users=users)

@app.route('/users/edit/<int:id>')
def edit(id):
    users=User.get_one(id)
    return render_template("edit.html", user=users)

@app.route('/users/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/show/<int:id>')
def show_one(id):
    users=User.get_one(id)
    print(users)
    return render_template("show_one.html", users=users)

@app.route('/users/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect ('/users')

            
if __name__ == "__main__":
    app.run(debug=True)