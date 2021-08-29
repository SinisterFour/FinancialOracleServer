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
