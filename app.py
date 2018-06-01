from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello heroku"

@app.route("/hello")
def hello():
    return "Hello Word!"

@app.route("/members")
def member():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

#
# @app.route("/")
# def index():
    # return "index!"
#
# @app.route("/hello")
# def hello():
    # return "Hello Word!"
#
# @app.route("/members")
# def hello():
    # return "Members"
#
# @app.route("/members/<string:name>/")
# def getMember(name):
    # return name
#
# if __name__ == "__main__":
    # app.run()
