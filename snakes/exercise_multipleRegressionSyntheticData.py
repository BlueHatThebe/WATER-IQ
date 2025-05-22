import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Set random seed for reproducibility
np.random.seed(0)

# Generate synthetic data
x1 = 10 * np.random.rand(100)  # Feature 1: random values between 0 and 10
x2 = 10 * np.random.rand(100)  # Feature 2: random values between 0 and 10
epsilon = np.random.normal(0, 1, 100)  # Noise: normal distribution, mean 0, std 1
y = 3 + 2 * x1 + 4 * x2 + epsilon  # Target variable

# Combine features into a 2D array
X = np.column_stack((x1, x2))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and fit the model
model = LinearRegression()
model.fit(X_train, y_train)

# Print intercept and coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Make predictions and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Check correlation between x1 and x2
corr = np.corrcoef(x1, x2)[0, 1]
print("Correlation between x1 and x2:", corr)