from ast import Num
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key='security_key'

@app.route('/')
def index():
    session["num"]=1
    return render_template("index.html")

@app.route('/count')

def count():
    session["num"]=session["num"]+1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")
if __name__=="__main__":
    app.run(debug=True)
