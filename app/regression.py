import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


class Regression:
    def __init__(self, X, y, link=None, dataset=None):
        self.X = X
        self.y = y
        self.link = link
        self.dataset = dataset

    # Esta es la buenona
    def linear(x, y, inpc):
        print("X:", x)
        x = numpy.asarray(x)
        y = numpy.asarray(y)

        model = LinearRegression().fit(x, y)

        information = dict()
        information["score"] = model.score(x, y)
        information["intercept"] = model.intercept_
        information["slope"] = model.coef_
        information["predict"] = model.predict([inpc])

        return information

    def linear_regression(self, x, y):
        return LinearRegression().fit(self.X, self.y)

    def train_linear_regression(df, x_name_dimension, y_name_dimension):
        X_train, X_test, y_train, y_test = train_test_split(
            df[x_name_dimension], df[y_name_dimension], test_size=0.2
        )

        linear_regression = LinearRegression().fit(
            X_train.values.reshape(-1, 1), y_train.values
        )

        info = dict()
        prediccion = linear_regression.predict(X_test.values.reshape(-1, 1))

        info["prediction"] = linear_regression.predict(np.array([[60]]))[0]
        info["score"] = linear_regression.score(
            X_test.values.reshape(-1, 1), y_test.values
        )
        info["mean_squared_error"] = mean_squared_error(y_test, prediccion)

        return linear_regression, info

    def polynomial_regression(self):
        poly_reg = PolynomialFeatures(degree=4)
        X_poly = poly_reg.fit_transform(self.X)
        pol_reg = LinearRegression()
        pol_reg.fit(X_poly, self.y)
        return [pol_reg, poly_reg]

    def vizualize_linear_regression(self, linear_regression):
        plt.scatter(self.X, self.y, color="red")
        plt.plot(self.X, linear_regression.predict(self.X), color="blue")
        plt.title("Linear Regression")
        plt.show()

    def vizualize_polynomial_regression(self, pol_reg, poly_reg):
        plt.scatter(self.X, self.y, color="red")
        plt.plot(self.X, pol_reg.predict(poly_reg.fit_transform(self.X)), color="blue")
        plt.title("Polynomial Regression")
        plt.show()
