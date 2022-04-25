
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key= 'dan the man'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/progress',methods = ['POST'])
def progress():
    session['name'] = request.form['name']
    session['city'] = request.form['city']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/info')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/goback')
def goBack():
    return render_template('index.html')
if __name__=="__main__":   
    app.run(debug=True)