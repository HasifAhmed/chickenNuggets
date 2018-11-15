from flask import Flask, render_template
from urllib.request import urlopen
import json
app = Flask(__name__)

@app.route("/")
def show():
    html = urlopen("https://api.nasa.gov/planetary/apod?api_key=x9CuMbqcX0mo5j5BF8pQGYaTx7R7dGSqSsOUQpmk")
    text = json.loads(html.read());
    return render_template("template.html",title = text['title'],
                            explanation = text['explanation'],
                            vid = text['url'])
app.debug = True
app.run()
