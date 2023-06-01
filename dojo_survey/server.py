from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key='123'
@app.route('/')
def index():
    return render_template("index.html")	# notice the 2 new named arguments!

@app.route('/form', methods=['POST'])
def form():
    print(request.form)
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comments']
    return redirect('/submitted')


@app.route('/submitted')
def submitted():
    
    return render_template("submitted.html")


if __name__=="__main__":
    app.run(debug=True)
