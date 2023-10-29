from django.http import JsonResponse
from rest_framework import viewsets,generics,filters
from games_database_api.models import Game,Genre,Franchise,Publisher,Developer,ProgrammingLanguage,GameEngine,GameProgrammingLanguage

from games_database_api.serializer import GameSerializer,GenreSerializer,FranchiseSerializer,GameGenre,DeveloperSerializer,PublisherSerializer,GameGenreSerializer,ListGameGenreSerializer,ListGameFranchiseSerializer,ListGameDeveloperSerializer,ListGamePublisherSerializer,ProgrammingLanguageSerializer,GameEngineSerializer,GameProgrammingLanguageSerializer,ListGameGameEngineSerializer,ListGameProgrammingLanguageSerializer
from django_filters.rest_framework import DjangoFilterBackend


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializer

class GameEngineViewSet(viewsets.ModelViewSet):
    queryset = GameEngine.objects.all()
    serializer_class = GameEngineSerializer

class GameProgrammingLanguageViewSet(viewsets.ModelViewSet):
    queryset = GameProgrammingLanguage.objects.all()
    serializer_class = GameProgrammingLanguageSerializer

class FranchiseViewSet(viewsets.ModelViewSet):
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer
class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
class GameGenreViewSet(viewsets.ModelViewSet):
    queryset= GameGenre.objects.all()
    serializer_class = GameGenreSerializer
class ListGameGenreViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = GameGenre.objects.filter(genre_id =self.kwargs['pk'])
        return queryset
    serializer_class = ListGameGenreSerializer
class ListGameProgrammingLanguageViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = GameProgrammingLanguage.objects.filter(programmingLanguage_id =self.kwargs['pk'])
        return queryset
    serializer_class = ListGameProgrammingLanguageSerializer
class ListGameGameEngineViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Game.objects.filter(gameEngine_id =self.kwargs['pk'])
        return queryset
    serializer_class = ListGameGameEngineSerializer
class ListGameFranchiseViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Game.objects.filter(franchise_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListGameFranchiseSerializer
class ListGameDeveloperViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Game.objects.filter(developer_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListGameDeveloperSerializer
class ListGamePublisherViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Game.objects.filter(publisher_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListGamePublisherSerializer

