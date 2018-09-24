import os
import random
import csv
from flask import Flask, render_template
import rme

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("occ.html", var1=file)

@app.route('/occupations')
def joblist():
    return render_template("occ.html",
                           title = "Title",
                           dictjobs = rme.read("csvv.csv"),
                           random = rme.retjob("csvv.csv")
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
