# Hasif Ahmed 
# SoftDev1 pd8
# K8 -- Fill Yer Flask 
# 2018-09-19
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return "<b>Welcome!</b> <a href = '/hasif'> Click here for Hasif</a>"

@app.route('/hasif')
def hasif():
    return "<b>I am Hasif Ahmed</b> <a href = '/route3'> Click here for route3</a>"

@app.route('/route3')
def route3():
    return "<b>This is route3</b> <a href = '/'> Back to Home </a>"

app.debug = True
app.run()
