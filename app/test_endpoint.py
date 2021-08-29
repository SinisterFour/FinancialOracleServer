import requests
import json


PROD = "TODO: SET THIS WHEN AVAILABLE"
LOCALHOST = "http://127.0.0.1:5000"


def get_polynomial_regression_test(environment):
    link = environment + "/polynomial_regression"
    params = {
        "train": [
            ["Columna1", "Columna2", "Columna3", "..."],
            [1, 1, 2000, 48.80116016],
            [2, 1, 2000, 49.1371793],
            [1, 2, 2000, 49.41320941],
            # 504 filas representando quincenas del 2000 al 2020
        ],
        "test": [
            ["Columna1", "Columna2", "Columna3", "..."],
            [1, 1, 2000, 48.80116016],
            [2, 1, 2000, 49.1371793],
            [1, 2, 2000, 49.41320941],
            # 15 filas
        ],
        "train_inpc": [0, 1, 2, 3, 2],  # 504 valores
        "test_inpc": [0, 1, 2, 3, 2],  # 15 valores
    }

    req = requests.get(url=link, json=params)
    data = req.json
    print(json.loads(req.content))


def get_linear_regression_test(environment):
    link = environment + "/linear_reggression"
    params = {"response": 42}

    req = requests.get(url=link, json=params)
    data = req.json
    print(json.loads(req.content))


get_linear_regression_test(LOCALHOST)
