from django.test import TestCase
import random
import string
from AppCoder.models import Profesor

from datetime import datetime as dt
from .utilities.utility import return_today

# Create your tests here.
class TestUtilities(TestCase):
    
    def test_day(self):
        hoy = dt.now()
        self.assertEqual(hoy.day, return_today())

class TestUsers(TestCase):

    def test_crear_profesor(self):
        informacion = {
            "apellido": "",
            "email": "coder@coder.com"
        }
        KEY_LEN = 20
        keylistNombre = [random.choice((string.ascii_letters + string.digits)) for i in range(KEY_LEN)]
        nombrePrueba = "".join(keylistNombre)

        print(f"----> Prueba con: {nombrePrueba}")

        profesor = Profesor(
            nombre=nombrePrueba,
            apellido=informacion["apellido"],
            email=informacion["email"],
        )
        profesor.save()
