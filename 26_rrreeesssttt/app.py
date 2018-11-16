#Hasif Ahmed
#SoftDev1 pd8
#K26 -- Getting More REST
#2018-11-16
from flask import Flask, render_template

import json
from urllib.request import urlopen

app = Flask(__name__)


@app.route("/")
def home():
    apis = {}

    #britni
    url = 'https://api.darksky.net/forecast/87c185b620c9ab832eb1ea5e37ff7a5f/37.8267,-122.4233'
    req = urlopen(url)
    dict = json.loads(req.read())
    apis['weather'] = ('Weather',dict)

    #vincent lin
    url = 'https://dog.ceo/api/breeds/image/random'
    req = urlopen(url)
    dict = json.loads(req.read())
    apis['dogs'] = ('Dogs', dict)

    #imad
    url = 'https://www.boredapi.com/api/activity'
    req = urlopen(url)
    dict = json.loads(req.read())
    apis['bored'] = ('Bored', dict)

    return render_template("template.html", **apis)

if __name__ == "__main__":
    app.debug = True
    app.run()
