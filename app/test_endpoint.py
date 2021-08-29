import requests
import json
import numpy as np
from sklearn.linear_model import LinearRegression

PROD = "TODO: SET THIS WHEN AVAILABLE"
LOCALHOST = "http://127.0.0.1:5000"

def get_linear_regression_test(environment):
    link = environment + "/linear_reggression"
    reader = np.genfromtxt("./datasets/imdb-movies-clean-data.csv", delimiter=",")
    
    params = {
        "train": [],
        "test": [],
        "train_inpc": [],
        "test_inpc": [],
    }

    params["train"] = reader[1:, :-2].tolist()  # Train
    params["train_inpc"] = reader[1:, -1:].tolist()  # Train inpc
    params["test_inpc"] = [153, 26435, 6000000, 1927]

    req = requests.get(url=link, json=params)
    # print(json.loads(req.content.decode("utf-8")))
    print(req.content.decode("utf-8"))


def get_polynomial_regression_test(environment):
    link = environment + "/linear_reggression"
    params = {
        "train": [
            ["Columna1", "Columna2", "Columna3", "..."],
            [1, 1, 2000, 48.80116016],
            [2, 1, 2000, 49.1371793],
            [1, 2, 2000, 49.41320941],
        ],
        "test": [
            ["Columna1", "Columna2", "Columna3", "..."],
            [1, 1, 2000, 48.80116016],
            [2, 1, 2000, 49.1371793],
            [1, 2, 2000, 49.41320941],
        ],
        "train_inpc": [0, 1, 2, 3, 2],
        "test_inpc": [0, 1, 2, 3, 2],
    }

    req = requests.get(url=link, json=params)
    data = req.json
    print(json.loads(req.content))


get_linear_regression_test(LOCALHOST)
