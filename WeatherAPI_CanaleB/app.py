from flask import Flask, render_template
from urllib.request import urlopen
import json
app = Flask(__name__)

@app.route("/")
def show():
    lat = 0
    longit = 0
    if "lat" not in request.args or "longit" not in request.args:
        flash("FILL OUT ALL FIELDS")
    elif request.args["lat"] == "" or abs(float(request.args["lat"])) > 90:
        flash("Latitude")
    elif request.args["longit"] == "" or abs(float(request.args["longit"])) > 180:
        flash("Longitude")
    else:
        lat = request.args["lat"]
        long = request.args["longit"]

    url = "https://api.darksky.net/forecast/7c8975f9610d0e7b761207ecd73d6287/37.8267,-122.4233/" + str(lat) + "," + str(longit)
    request = urlopen(url)
    dict = json.loads(request.read())
    return render_template("template.html",timezone = dict["timezone"],
        summary = dict["currently"]["summary"],
        icon = dict["currently"]["icon"],
        temp = dict["currently"]["temperature"],
        precipProb=dict["currently"]["precipProbability"])
app.debug = True
app.run()
