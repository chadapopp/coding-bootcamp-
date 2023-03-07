from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)  

img_folder = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = img_folder

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    num1 = request.form['strawberry']
    num2 = request.form['raspberry']
    num3 = request.form['apple']
    num = int(num1) +int(num2) + int(num3)
    print(f"Charging {first_name} for {(num)} fruits.")
    
    return render_template("checkout.html",first_name = first_name, last_name = last_name, student_id = student_id, num = num, num1=num1, num2=num2, num3=num3)

@app.route('/fruits')         
def fruits():
    img_list = os.listdir('static/img')
    img_list = ['img/' + img for img in img_list]
    return render_template("fruits.html",img_list=img_list)

if __name__=="__main__":   
    app.run(debug=True)    