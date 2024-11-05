import unittest
import numpy as np
import joblib
from src.predict import model

class TestPredict(unittest.TestCase):
    def test_prediction(self):
        new_data = np.random.rand(1, 20)
        prediction = model.predict(new_data)
        self.assertIn(prediction[0], [0, 1])

if __name__ == '__main__':
    unittest.main()
