import unittest
import numpy as np
import sys, os
from app import app, model



#python -m unittest test_app -v

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ph_out_of_range(self):
        result = self.app.post('/predict', data=dict(
            ph=15,
            hardness=150,
            solids=20000,
            chloramines=7,
            sulfate=300,
            conductivity=400,
            organic_carbon=10,
            trihalomethanes=60,
            turbidity=3
        ))
        self.assertEqual(result.status_code, 400)  