from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return "This is the home page"

@app.route('/hasif')
def hasif():
    return "I am Hasif Ahmed"

@app.route('/route3')
def route3():
    return "This is the third route"

app.debug = True
app.run()
