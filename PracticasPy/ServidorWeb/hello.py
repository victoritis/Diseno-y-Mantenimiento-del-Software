from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about_us/")
def about_us():
    return "<p>Sobre nosotros</p>"



from markupsafe import escape



@app.route("/hello/<name>")
def hello(name):
    return f"Hello,{escape(name)}!"






