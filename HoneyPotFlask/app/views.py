from app import app
from app.models import dbOperator
from flask import render_template,request,jsonify
import hashlib
import time

@app.route('/index',methods=['POST','GET'])
def index():

    db = dbOperator(DBName = "TestOne",CName ="Student")
    get = db.find_one()

    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():

    getDataUname = request.form['uname']
    getDataPword = request.form['pword']

    linkData = getDataUname + getDataPword
    md5Sum = hashlib.md5(linkData).hexdigest()

    data = {"id":"1",
            "uname":getDataUname,
            "pword":getDataPword,
            "time":str(time.time()),
            "sha1":md5Sum
        }
    db = dbOperator("WYUSEC","Login")

    db.insert(data)

    msg = "Invalid Username or Password"
    return msg
