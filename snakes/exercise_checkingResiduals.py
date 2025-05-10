import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Set random seed for reproducibility
np.random.seed(0)

# Generate sample data
X = 2 * np.random.rand(100, 1)  # 100 samples, 1 feature
y = 4 + 3 * X + np.random.randn(100, 1)  # Linear relationship with noise

# Flatten y to ensure it's 1D
y = y.ravel()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate residuals
residuals = y_test - y_pred

# Plot residuals vs. predicted values (check homoscedasticity)
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuals, color='blue')
plt.title('Residuals vs. Predicted')
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.axhline(y=0, color='red', linestyle='--')
plt.savefig('residuals_vs_predicted.png')
plt.close()  # Close the figure to free memory

# Plot residuals distribution (check normality)
plt.figure(figsize=(8, 6))
sns.histplot(residuals, kde=True, color='blue', bins=30)
plt.title('Residuals Distribution')
plt.xlabel('Residual')
plt.ylabel('Frequency')
plt.savefig('residuals_distribution.png')
plt.close()  # Close the figure to free memory

print("Plots saved successfully as 'residuals_vs_predicted.png' and 'residuals_distribution.png'")