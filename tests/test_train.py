import unittest
import joblib
from src.train_model import model

class TestModel(unittest.TestCase):
    def test_model(self):
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
