from rest_framework.test import APITestCase
from games_database_api.models import Game,Franchise,Developer,GameEngine,Publisher
from django.urls import reverse
from rest_framework import status
class GameTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Game-list')
        self.game_1 = Game.objects.create(name = 'Game_Teste_1',release_date = '2023-11-25',franchise=Franchise.objects.create(name='teste_1'),developer=Developer.objects.create(name='teste_1'),gameEngine=GameEngine.objects.create(name='teste_1'),publisher=Publisher.objects.create(name='teste_1'))
        self.game_2 = Game.objects.create(name = 'Game_Teste_2',release_date = '2023-11-25',franchise=Franchise.objects.create(name='teste_2'),developer=Developer.objects.create(name='teste_2'),gameEngine=GameEngine.objects.create(name='teste_2'),publisher=Publisher.objects.create(name='teste_2'))
    
    def test_get_games(self):
        """ Teste para GET de gêneros """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_post_games(self):
        """ Teste para POST de gênero """
        data = {
            "name":"Gênero_Teste_3",
            "release_date": '2023-11-25',
            "franchise": Franchise.objects.create(name='teste_3').pk,
            "developer": Developer.objects.create(name='teste_3').pk,
            "gameEngine": GameEngine.objects.create(name='teste_3').pk,
            "publisher": Publisher.objects.create(name='teste_3').pk
        }
        response = self.client.post(self.list_url,data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)   
    
    def test_delete_games(self):
        """ Teste para DELETE de gênero """
        response = self.client.delete(reverse('Game-detail', kwargs={'pk': self.game_1.pk}))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)