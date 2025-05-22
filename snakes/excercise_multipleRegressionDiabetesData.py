import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the diabetes dataset
diabetes = load_diabetes()
X = diabetes.data  # All 10 features
y = diabetes.target  # Disease progression

# Simple Linear Regression with BMI (feature index 2)
X_simple = X[:, 2].reshape(-1, 1)  # Reshape to 2D array
X_train_simple, X_test_simple, y_train, y_test = train_test_split(X_simple, y, test_size=0.2, random_state=0)

model_simple = LinearRegression()
model_simple.fit(X_train_simple, y_train)
y_pred_simple = model_simple.predict(X_test_simple)
mse_simple = mean_squared_error(y_test, y_pred_simple)
r2_simple = model_simple.score(X_test_simple, y_test)
print("Simple Linear Regression (BMI only) - MSE:", mse_simple, "R-squared:", r2_simple)

# Multiple Linear Regression with all features
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model_multiple = LinearRegression()
model_multiple.fit(X_train, y_train)
y_pred_multiple = model_multiple.predict(X_test)
mse_multiple = mean_squared_error(y_test, y_pred_multiple)
r2_multiple = model_multiple.score(X_test, y_test)
print("Multiple Linear Regression (all features) - MSE:", mse_multiple, "R-squared:", r2_multiple)

# Print coefficients for multiple regression
print("Coefficients:", model_multiple.coef_)