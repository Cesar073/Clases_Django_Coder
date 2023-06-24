from django.test import TestCase

from datetime import datetime as dt
from .utilities.utility import return_today

# Create your tests here.
class TestUtilities(TestCase):
    
    def test_day(self):
        hoy = dt.now()
        self.assertEqual(hoy.day, return_today())
