import json
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from flask import Flask, render_template, request
from app import app
from app.regression import *

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return {"response": 200}


@app.route("/linear_reggression", methods=["POST"])
def linear_regression():
    if request.data:
        parameters = json.loads(request.data.decode("utf-8"))
        train_matrix = parameters["body"]["trainMatrix"]
        train_INPC = parameters["body"]["trainINPC"]
        test_matrix = parameters["body"]["testMatrix"]
        test_INPC = parameters["body"]["testINPC"]
        
        model = LinearRegression().fit(train_matrix, train_INPC)
        forecast = model.predict(test_matrix)
        
        return {
            "forecast": forecast.tolist(),
            "mean_absolute_error": mean_absolute_error(test_INPC, forecast),
            "coefficient_of_determination": r2_score(test_INPC, forecast)
        }

    return {"Nothing to show": 400}


@app.route("/decision_tree", methods=["POST"])
def decision_tree():
    if request.data:
        parameters = json.loads(request.data.decode("utf-8"))
        train_matrix = parameters["body"]["trainMatrix"]
        train_INPC = parameters["body"]["trainINPC"]
        test_matrix = parameters["body"]["testMatrix"]
        test_INPC = parameters["body"]["testINPC"]
        
        model = DecisionTreeRegressor().fit(train_matrix, train_INPC)
        forecast = model.predict(test_matrix)
        
        return {
            "forecast": forecast.tolist(),
            "mean_absolute_error": mean_absolute_error(test_INPC, forecast),
            "coefficient_of_determination": r2_score(test_INPC, forecast)
        }

    return {"Nothing to show": 400}


@app.route("/neural_network", methods=["POST"])
def neural_network():
    if request.data:
        parameters = json.loads(request.data.decode("utf-8"))
        train_matrix = parameters["body"]["trainMatrix"]
        train_INPC = parameters["body"]["trainINPC"]
        test_matrix = parameters["body"]["testMatrix"]
        test_INPC = parameters["body"]["testINPC"]
        
        model = MLPRegressor(random_state=1).fit(train_matrix, train_INPC)
        forecast = model.predict(test_matrix)
        
        return {
            "forecast": forecast.tolist(),
            "mean_absolute_error": mean_absolute_error(test_INPC, forecast),
            "coefficient_of_determination": r2_score(test_INPC, forecast)
        }

    return {"Nothing to show": 400}


@app.route("/polynomial_regression", methods=["GET"])
def polynomial_regression():
    if request.data:
        parameters = json.loads(request.data.decode("utf-8"))
        return {"response": 200}

    return {"Nothing to show": 400}
