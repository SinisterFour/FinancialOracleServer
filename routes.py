from app import app
from flask import render_template, request


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/linear_reggression", methods=["GET"])
def linear_regression():
    parameters = request.data
    print("----------------------------------", parameters)
    return {"Response goes here": 0}


@app.route("/polynomial_regression", methods=["GET"])
def polynomial_regression():
    return {"Response goes here": 0}
