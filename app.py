from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Flask App!"

@app.route("/hello/<string:name>/")
def hello(name):
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis Von Neumann",
               "'Computer science is no more about computers than astronomy is about telescopes' -- Edsger Dijkastra",
               "'To understand recursion you first understand recursion...' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the science.' -- Galileo Galilei",
               "'Not everyone will understand your journey. That's fine. Its not their journey to make sense of. Its yours.' -- Unknown" ]

    randonnumber = randint(0,len(quotes)-1)
    quote = quotes[randonnumber]

    return render_template(
        'test.html', **locals())

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

