
#Indeed: Sarar Aseer, Hasif Ahmed
#SoftDev1 pd8
#K10 -- Jinja Tuning
#2018-09-24

import csv
from flask import Flask, render_template
from util import rme

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Indeed."

@app.route('/occupations')
def joblist():
    return render_template("occ.html",
                           title = "Jobs",
                           heading = "The purpose of this website is to select a random occupation from the table below and display it.",
                           dictjobs = rme.read("data/csvv.csv"),
                           random = rme.retjob("data/csvv.csv")
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
