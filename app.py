from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Flask App!"

# @app.route("/hello")
# def hello():
#     return "Hello Word!"
#
# @app.route("/members")
# def member():
#     return "Members"
#
@app.route("/members/<string:name>/")
def getMember(name):
    return render_template(
        'test.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
