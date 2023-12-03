from rest_framework.test import APITestCase
from games_database_api.models import Genre
from django.urls import reverse
from rest_framework import status
class GenreTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Genre-list')
        self.genre_1 = Genre.objects.create(name = 'Gênero_Teste_1')
        self.genre_2 = Genre.objects.create(name = 'Gênero_Teste_2')
    def test_get_generos(self):
        """ Teste para GET de gêneros """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_post_genero(self):
        """ Teste para POST de gênero """
        data = {
            "name":"Gênero_Teste_3"
        }
        response = self.client.post(self.list_url,data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)   
    def test_delete_genero(self):
        """ Teste para DELETE de gênero """
        response = self.client.delete(reverse('Genre-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)