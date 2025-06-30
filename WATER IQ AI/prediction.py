import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import json
import datetime

# Load data from JSON file
with open('sensor_data.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data['readings'])

# Convert timestamp to datetime and sort
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values('timestamp')

# Feature engineering
df['hour'] = df['timestamp'].dt.hour
df['temp_humidity_interaction'] = df['temperature'] * df['humidity']

# Define features (X) and target (y)
X = df[['temperature', 'humidity', 'distance', 'hour', 'temp_humidity_interaction']]
y = df['soil_moisture']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Linear Regression ---
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_y_pred = lr_model.predict(X_test)
lr_mse = mean_squared_error(y_test, lr_y_pred)
lr_r2 = r2_score(y_test, lr_y_pred)
print("Linear Regression - MSE:", lr_mse)
print("Linear Regression - R-squared:", lr_r2)

# --- Random Forest Regressor ---
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)
rf_mse = mean_squared_error(y_test, rf_y_pred)
rf_r2 = r2_score(y_test, rf_y_pred)
print("Random Forest - MSE:", rf_mse)
print("Random Forest - R-squared:", rf_r2)

# Visualization for Random Forest
plt.figure(figsize=(10, 6))
plt.scatter(y_test, rf_y_pred, color='blue', label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Perfect Prediction')
plt.xlabel('Actual Soil Moisture')
plt.ylabel('Predicted Soil Moisture')
plt.title('Random Forest: Actual vs Predicted Soil Moisture')
plt.legend()
plt.grid(True)
plt.show()

# Function to predict soil moisture for new data
def predict_soil_moisture(temperature, humidity, distance, hour=None):
    try:
        if hour is None:
            hour = datetime.datetime.now().hour
        temp_humidity_interaction = temperature * humidity
        new_data = pd.DataFrame({
            'temperature': [temperature],
            'humidity': [humidity],  # Fixed typo from 'humi dity'
            'distance': [distance],
            'hour': [hour],
            'temp_humidity_interaction': [temp_humidity_interaction]
        })
        prediction = rf_model.predict(new_data)
        return prediction[0]
    except Exception as e:
        print(f"Error in prediction: {e}")
        return None

# Example usage
new_temperature = 25.5
new_humidity = 58.8
new_distance = 9.5
predicted_soil_moisture = predict_soil_moisture(new_temperature, new_humidity, new_distance)
if predicted_soil_moisture is not None:
    print(f"Predicted soil moisture for temp={new_temperature} C, humidity={new_humidity}%, distance={new_distance}cm: {predicted_soil_moisture}")
else:
    print("Prediction failed.")