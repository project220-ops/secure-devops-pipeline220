import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import joblib

# Generate synthetic data
X = np.random.rand(1000, 20)
y = np.random.randint(2, size=1000)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model.pkl')
