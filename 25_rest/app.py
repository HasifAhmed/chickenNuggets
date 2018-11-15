from flask import Flask, render_template, request,redirect
from urllib.request import urlopen
import json

app = Flask(__name__)

url = "https://http.cat/"
L = ["100", "101","200","202","204","206","207","300","301","302","303","304",
"305","307","400","401","402","403","404","405","406","408","409","410","411",
"412","413","414","415","416","417","418","420","421","422","423","424","425",
"426","429","431","444","450","451","500","502","503","504","506","507","508",
"509","510","511","599"]
@app.route("/")
def home():
    return render_template("template.html");

@app.route("/res")
def show():
    search = request.args["error"]
    if search not in L:
        search = "404"

    print("----------------")
    print(search)
    print("----------------")


    return render_template("results.html",img = url + search, num = int(search))



app.debug = True
app.run()
