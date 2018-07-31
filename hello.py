from flask import Flask, flash, redirect, render_template, request, session, abort
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from random import randint 

DEBUG = True
app = Flask(__name__)
app.secret_key = 'ThisisSuperSecret2346242235293hd' 
app.config.from_object(__name__)
master = 'dogdog'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

@app.route("/")
def index():
    return "Flask App!"
 
@app.route("/hello/<string:name>/")
def hello(name):
    quotes = [ "'lize how complicated life is.' -- John Louis von Neumann ",
               "'Comp than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To ucursion you must first understand recursion..' -- Unknown",
               "'You m of things that never were and ask, why not?' -- Unknown",
               "'Mathmatics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not t their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]
    return render_template(
        'test.html',**locals())

@app.route("/sessionSet")
def ss():
    session['key'] = 0
    return "Key Set to 0"

@app.route("/sessionPrint")
def sp():
    return "New Key Value: " + str(session['key'])

@app.route("/sessionMore")
def sm():
    session['key'] = session['key'] + 1
    return "Key Value Increased"

@app.route("/form", methods=['GET','POST'])

def frm():
    return render_template('form.html')

@app.route("/result", methods=['GET','POST'])
def result():
    if request.method == 'POST':
        result = request.form
        session['Key'] = result["key"]
        return render_template("results.html",result=result)

@app.route("/auth")
def auth():
    global master
    if master == session['Key']:
        session['Log'] = True
        return "Successful Log In"
    else:
        session['Log'] = False
        return "Failed Log In"

@app.route("/authCheck")
def chk():
    if not session['Log']:
        return render_template("fail.html")
    else:
        return "SUCCESSFUL ENTRY"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
