import requests
import json


PROD = "TODO: SET THIS WHEN AVAILABLE"
LOCALHOST = "http://127.0.0.1:5000"


def get_polynomial_regression_test(environment):
    link = environment + "/polynomial_regression"
    params = {"response": 42}

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
