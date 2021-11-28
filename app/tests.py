from django.test import TestCase
from django.contrib.auth.models import User

# REST
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate


class TestEnquete(APITestCase):
    url = 'http://127.0.0.1:8000/api/enquetes/'

    teste = {"titulo": "TestEnquete",
             "texto": "testes no test.py",
             "respostas": [
                 {"opcao": "pode ser que de certo"},
                 {"opcao": "pode ser que não de certo"}
             ]
             }


    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user(
            'usuarioteste', email='teste@teste.com.br', password='123456'
        )
        self.user.save()

    def teste_nao_cria_enquete(self):
        response = self.client.post(self.url, self.teste, format='json')

        self.assertEquals(response.status_code, 401)

    def teste_cria_enquete(self):
        self.client.login(username='usuarioteste', password='123456')

        response = self.client.post(self.url, self.teste, format='json')
        self.assertEquals(response.status_code, 201)
