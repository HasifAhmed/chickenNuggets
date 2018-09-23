from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    return "This is the homepage"

@app.route('/occupations')
def joblist():
    return render_template('occ.html')

app.debug = True
app.run()
