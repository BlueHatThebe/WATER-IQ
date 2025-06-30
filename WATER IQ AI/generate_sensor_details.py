import datetime
import random
import json

def generate_readings():
    start_time = datetime.datetime(2025, 6, 30, 8, 0, 0)
    readings = []
    distance = 10.0  # Initial distance in cm

    for i in range(145):  # 145 readings from 8:00 AM to 8:00 PM
        current_time = start_time + datetime.timedelta(minutes=5 * i)
        timestamp = current_time.isoformat() + "+02:00"  # SAST timezone

        # Calculate base temperature and humidity
        if i <= 72:  # 8:00 AM to 2:00 PM
            temperature = 20 + 10 * (i / 72)  # Increase from 20°C to 30°C
            humidity = 60 - 10 * (i / 72)     # Decrease from 60% to 50%
        else:  # 2:00 PM to 8:00 PM
            temperature = 30 - 10 * ((i - 72) / 72)  # Decrease from 30°C to 20°C
            humidity = 50 + 10 * ((i - 72) / 72)     # Increase from 50% to 60%

        # Add random noise
        temperature += random.uniform(-0.5, 0.5)
        humidity += random.uniform(-1, 1)

        # Update distance with small random change, clamped between 5 and 15 cm
        distance_change = random.uniform(-0.5, 0.5)
        distance = max(5, min(15, distance + distance_change))

        # Calculate soil moisture with a formula and noise, clamped between 200 and 500
        soil_moisture = 500 - 10 * temperature + 5 * humidity - 20 * distance + random.uniform(-20, 20)
        soil_moisture = max(200, min(500, soil_moisture))

        # Round values to appropriate precision
        readings.append({
            "timestamp": timestamp,
            "temperature": round(temperature, 1),
            "humidity": round(humidity, 1),
            "distance": round(distance, 1),
            "soil_moisture": int(soil_moisture)
        })

    return readings

# Generate the readings
readings = generate_readings()

# Save to JSON file
with open('sensor_data.json', 'w') as f:
    json.dump({"readings": readings}, f, indent=2)

print("Generated 'sensor_data.json' with 145 readings from 8:00 AM to 8:00 PM, including lower temperatures.")