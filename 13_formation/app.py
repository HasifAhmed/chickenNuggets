from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def homepage():
    print(app)
    return render_template("template.html",
                           title = "Welcome!",
                           head = "Please Input A Username In The Box Below",
                           inputype = "Username: "
                           )

@app.route('/greetings', methods = ["GET","POST"])
def greet():
    print(app)
    print(request)
    print(request.method)
    print(request.form)
    return render_template("greeting.html",
                           title = "Greetings",
                           head = "Greetings " + request.form['username'] + "!",
                           inputype = "The method type is: " + request.method
                           )
                           
if __name__ == '__main__':
    print(app)
    app.debug = True
    app.run()

