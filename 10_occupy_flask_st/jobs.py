from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    return "This is the homepage"

@app.route('/occupations')
def joblist(hello = NONE, foo = NONE   ):
    return render_template('occ.html', hello = "hello", foo = "foo")

app.debug = True
app.run()
