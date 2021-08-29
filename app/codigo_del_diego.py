import numpy as np
from sklearn.linear_model import LinearRegression

reader = np.genfromtxt("./datasets/imdb-movies-clean-data.csv", delimiter=",")
x = reader[1:, :-2]  # Train
y = reader[1:, -1:]  # Train inpc

print("X:", x, "\n")
print("lle:", y, "\n")

model = LinearRegression().fit(x, y)

print("coefficient of determination:", model.score(x, y))
print("intercept:", model.intercept_)
print("slope:", model.coef_)

# Aqui va test INPC
pred = model.predict([[153, 26435, 6000000, 1927]])
print("predicted response:", pred)
