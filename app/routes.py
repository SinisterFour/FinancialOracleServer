import json
from app import app
from flask import render_template, request


@app.route("/")
@app.route("/index")
def index():
    return {"response": 200}


@app.route("/linear_reggression", methods=["GET"])
def linear_regression():
    if request.data:
        parameters = json.loads(request.data.decode("utf-8"))
        return {"response": 200}

    return {"Nothing to show": 400}


@app.route("/polynomial_regression", methods=["GET"])
def polynomial_regression():
    if request.data:
        parameters = json.loads(request.data.decode("utf-8"))
        return {"response": 200}

    return {"Nothing to show": 400}
