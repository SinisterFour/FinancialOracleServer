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

    def linear_regression(self):
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


# Dataset handle
data_link = "https://s3.us-west-2.amazonaws.com/public.gamelab.fun/dataset/position_salaries.csv"
dataset = pd.read_csv(data_link)
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Linear and polynomial regressions
reg = Regression(X, y)
linear_regression = reg.linear_regression()
pol_reg, poly_reg = reg.polynomial_regression()

# train_linear_regression
df = pd.read_csv("./datasets/genero.txt", delimiter=",")
lr, info = Regression.train_linear_regression(df, "Height", "Weight")
