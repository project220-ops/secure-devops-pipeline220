import numpy as np
import joblib

# Load the model
model = joblib.load('model.pkl')

# Predict on new data
new_data = np.random.rand(1, 20)
prediction = model.predict(new_data)
print(f'Prediction: {prediction}')
