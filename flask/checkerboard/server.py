from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",row=8,col=8,color_1='red',color_2='black')

@app.route('/<int:x>')
def row(x):
    return render_template("index.html",row=x,col=8,color_1='red',color_2='black')

@app.route('/<int:x>/<int:y>')
def col(x,y):
    return render_template("index.html",row=x,col=y,color_1='red',color_2='black')

@app.route('/<int:x>/<int:y>/<string:new_color1>')
def new_color1(x,y,new_color1):
    return render_template("index.html",row=x,col=y,color_1=new_color1,color_2='black')

@app.route('/<int:x>/<int:y>/<string:new_color1>/<string:new_color2>')
def new_color2(x,y,new_color1,new_color2):
    return render_template("index.html",row=x,col=y,color_1=new_color1,color_2=new_color2)

if __name__ =="__main__":
    app.run(debug=True)






