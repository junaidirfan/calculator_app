"""Unit tests for Flask Calculator App"""

import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    """Test cases for the Flask calculator routes"""

    def setUp(self):
        """Set up the test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        """Test addition operation via POST"""
        response = self.app.post("/", data={"num1": "10", "num2": "5", "operation": "add"})
        self.assertIn(b"15", response.data)

    def test_subtraction(self):
        """Test subtraction operation via POST"""
        response = self.app.post("/", data={"num1": "10", "num2": "5", "operation": "subtract"})
        self.assertIn(b"5", response.data)

    def test_multiplication(self):
        """Test multiplication operation via POST"""
        response = self.app.post("/", data={"num1": "10", "num2": "5", "operation": "multiply"})
        self.assertIn(b"50", response.data)

    def test_division(self):
        """Test division operation via POST"""
        response = self.app.post("/", data={"num1": "10", "num2": "0", "operation": "divide"})
        self.assertIn(b"2", response.data)

    def test_divide_by_zero(self):
        """Test division by zero via POST"""
        response = self.app.post("/", data={"num1": "10", "num2": "0", "operation": "divide"})
        self.assertIn(b"Cannot divide by zero", response.data)

if __name__ == "__main__":
    unittest.main()

