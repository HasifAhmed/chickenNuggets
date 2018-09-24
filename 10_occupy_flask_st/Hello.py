#Indeed: Sarar Aseer, Hasif Ahmed
#SoftDev1 pd8
#K10 -- Jinja Tuning
#2018-09-24

import os
import random
import csv
from flask import Flask, render_template
import rme

app = Flask(__name__)


@app.route('/')
def homepage():
    return "Indeed."

@app.route('/occupations')
def joblist():
    return render_template("occ.html",
                           title = "Jobs",
                           title2 = "Percentages",
                           dictjobs = rme.read("csvv.csv"),
                           random = rme.retjob("csvv.csv")
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
