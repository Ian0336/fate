import lday as lun
import datetime
import sys
from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/show")
def show():
    year=int(request.args.get("year"))
    month=int(request.args.get("month"))
    day=int(request.args.get("day"))
    hour=int(request.args.get("hour"))
    if not 0<month<=12 or not 0<day<=31 or not 0<=hour<=24:
        return render_template("failure.html")
    
    lun.mm(year, month, day, hour)
    listg=lun.listg
    listz=lun.listz
    
    listy=lun.listy
    listm=lun.listm
    listd=lun.listd
    listh=lun.listh
    
    
    
    
    return render_template("show.html", listg=listg, listz=listz, listy=listy, listd=listd, listh=listh, listm=listm)
    
    
    
    
    
"""year=int(input("出生年:"))
month=int(input("出生月:"))
day=int(input("出生日:"))
hour=int(input("出生時(小時):"))

"""
