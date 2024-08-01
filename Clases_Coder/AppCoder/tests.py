from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from AppCoder.models import Profesor

# Create your tests here.
class EliminarProfesorTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.profesor = Profesor.objects.create(
            nombre="Juan",
            apellido="Perez",
            email="a@b.com"
        )
        self.url = reverse("ProfesorDelete", args=[self.profesor.id])

    def test_eliminar_profesor(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, "AppCoder/profesor_confirm_delete.html")
        self.client.post(self.url)
        self.assertQuerysetEqual(Profesor.objects.all(), [])
