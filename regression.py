import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


class Regression:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def linear_regression(self):
        return LinearRegression().fit(self.X, self.y)

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


dataset = pd.read_csv(
    "https://s3.us-west-2.amazonaws.com/public.gamelab.fun/dataset/position_salaries.csv"
)
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

reg = Regression(X, y)

linear_regression = reg.linear_regression()
pol_reg, poly_reg = reg.polynomial_regression()
reg.vizualize_linear_regression(linear_regression)
# reg.vizualize_polynomial_regression(poly_reg, poly_reg)
