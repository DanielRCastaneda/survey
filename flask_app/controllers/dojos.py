from flask import Flask, render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/progress',methods = ['POST'])
def progress():
    if   Dojo.validate_info(request.form):
        Dojo.save(request.form)
        return redirect('/info')
    print(request.form)
    return redirect('/')

@app.route('/info')
def info():
    return render_template('info.html', survey = Dojo.get_last_survey())

@app.route('/goback')
def goBack():
    return render_template('index.html')