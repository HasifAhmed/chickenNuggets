from flask import Flask
from urllib.request import urlopen

app = Flask(__name__)

html = urlopen("https://api.nasa.gov/planetary/apod?api_key=QtXGjoKMEUOqxPxyeh9vqi9F2G6eeMHH4OEy1ovZ")

if __name__ == "__name__":
    app.debug = True
    app.run()
