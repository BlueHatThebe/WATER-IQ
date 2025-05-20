import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data: y = x^2 + 0.5x + noise
X = np.linspace(-3, 3, 100).reshape(-1, 1)  # Feature vector
y = X**2 + 0.5 * X + np.random.normal(0, 1, X.shape)  # Quadratic data with noise

# Define a function to perform k-fold cross-validation for different polynomial degrees
def cross_validate_degrees(X, y, degrees, folds=5):
    """
    Perform k-fold cross-validation for polynomial regression models of different degrees.
    
    Parameters:
    - X: Feature matrix
    - y: Target vector
    - degrees: List of polynomial degrees to evaluate
    - folds: Number of folds for cross-validation (default: 5)
    
    Returns:
    - cv_errors: List of average MSE for each degree
    """
    kf = KFold(n_splits=folds, shuffle=True, random_state=42)
    cv_errors = []
    for degree in degrees:
        mse_list = []
        for train_index, val_index in kf.split(X):
            # Split data into training and validation sets
            X_train, X_val = X[train_index], X[val_index]
            y_train, y_val = y[train_index], y[val_index]
            
            # Create and fit the polynomial regression model
            polyreg = make_pipeline(PolynomialFeatures(degree), LinearRegression())
            polyreg.fit(X_train, y_train.ravel())
            
            # Predict on validation set and compute MSE
            y_pred = polyreg.predict(X_val)
            mse = mean_squared_error(y_val, y_pred)
            mse_list.append(mse)
        
        # Store the average MSE for this degree
        cv_errors.append(np.mean(mse_list))
    return cv_errors

# Define the range of degrees to test
degrees = range(1, 11)

# Perform cross-validation
cv_errors = cross_validate_degrees(X, y, degrees)

# Find the degree with the lowest cross-validation error
optimal_degree = degrees[np.argmin(cv_errors)]
print(f"Optimal polynomial degree: {optimal_degree}")

# Plot cross-validation errors for each degree
plt.figure(figsize=(8, 5))
plt.plot(degrees, cv_errors, marker='o', color='blue')
plt.xlabel('Polynomial Degree')
plt.ylabel('Cross-Validation MSE')
plt.title('Cross-Validation Error vs. Polynomial Degree')
plt.grid(True)
plt.show()

# Fit the polynomial regression model with the optimal degree
polyreg_optimal = make_pipeline(PolynomialFeatures(optimal_degree), LinearRegression())
polyreg_optimal.fit(X, y.ravel())

# Predict using the optimal model
y_pred_optimal = polyreg_optimal.predict(X)

# Plot the data and the optimal polynomial fit
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Data', alpha=0.5)
plt.plot(X, y_pred_optimal, color='red', label=f'Optimal Degree {optimal_degree} Fit')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()