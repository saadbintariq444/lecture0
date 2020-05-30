import datetime

from flask import Flask, render_template, request, session
from flask_session import Session


app=Flask(__name__)


#@app.route("/")
#def index():
#    return ("Hello world")

#@app.route("/david")
#def myfunc1():
#    return '<h1>Hello Saad</h1>'

#@app.route('/<name>')
#def myfunc2(name):
#    name=name.capitalize()
#    return '<h1>Hello {} </h1>'.format(name)

#@app.route('/<string:name>')
#def myfunc3(name):
#    return f'<h2>Hello func3 {name} </h2>'

#//////////////////////////////////////////////////////////////////////////////
#@app.route("/home")
#def homie():
#    return render_template("index.html")

#@app.route("/about")
#def abutie():
#    myheading='hello i am from python displaying on html'
#    return render_template("about.html",myheading=myheading)
#------------------------------------------------------------------------------
#@app.route("/isiteid")
#def eidi():
#    now=datetime.datetime.now()
#    eid=now.month==5 and now.day==25
#    return render_template("eid.html",eid=eid)
#------------------------------------------------------------------------------
#@app.route("/loop")
#def loopi():
#    names=['Saad','Ali','Rajab']
#    return render_template("loops.html",names=names)
#////////////////////Tempalte 0 ended/////////////////////////////////////////
#--------------------------------using urls------------------------------------
#@app.route("/mypage")
#def index():
#    return render_template("mypage.html")
#@app.route("/more")
#def more():
#    return render_template("more.html")

#--------------------------------------using layout1-------------------------------
#@app.route("/mypage")
#def index():
#    return render_template("index.html")
#@app.route("/more")
#def more():
#    return render_template("more.html")
#////////////////////Tempalte 1 ended/////////////////////////////////////////


#----------------------start of template 2------------------------------------
#@app.route("/")
#def index():
#    return render_template("index.html")

#@app.route("/hello", methods=["GET","POST"])
#def hello():
#    if request.method=="GET":
#        return "Donot press enter , sumit the form by button"
#    name=request.form.get("name")
#    return render_template("hello.html",name=name)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)
#notes=[]
@app.route("/", methods=["GET","POST"])
def index():
#session["notes"]=[]
    if session.get("notes") is None:
         session["notes"]=[]
    if request.method=="POST":
         note=request.form.get("note")
#notes.append(note)
         session["notes"].append(note)
    #return render_template("index.html",notes=notes)

    return render_template("index.html",notes= session["notes"])
